import base64
import json
import requests
import os
import io
import re

from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from diseases import get_disease_info, get_severity_level

# -------------------- LOAD ENV --------------------
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY not found!")

# -------------------- APP INIT --------------------
app = Flask(__name__)
CORS(app, origins="*")

# -------------------- SAFE API CALL --------------------
def call_groq(payload):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        GROQ_URL, headers=headers, json=payload
    )
    data = response.json()
    if "choices" not in data:
        raise Exception(f"Groq API Error: {data}")
    return data["choices"][0]["message"]["content"]


# -------------------- DEFAULT RESPONSE --------------------
def default_response():
    return {
        "crop_type": "unknown",
        "disease_detected": "Unable to analyze",
        "confidence": 0,
        "severity": "Low",
        "visible_symptoms": ["Could not detect symptoms"],
        "affected_area_percent": 0,
        "immediate_action": "Please try with a clearer photo",
        "description": "Could not analyze this image"
    }


# -------------------- ANALYZE CROP IMAGE --------------------
def analyze_crop_image(base64_image):
    prompt = """You are an expert agricultural scientist
specializing in crop diseases in Nepal and South Asia.
Analyze this crop image and respond ONLY with this exact JSON:
{
  "crop_type": "tomato/potato/rice/wheat/maize/other",
  "disease_detected": "disease name or Healthy Crop",
  "confidence": 95,
  "severity": "High/Medium/Low/None",
  "visible_symptoms": ["symptom 1", "symptom 2"],
  "affected_area_percent": 30,
  "immediate_action": "what farmer should do right now",
  "description": "brief description of what you see"
}"""

    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    }

    text = call_groq(payload)
    print("AI Response:", text)

    clean = text.replace(
        "```json", "").replace("```", "").strip()

    if not clean:
        return default_response()

    try:
        return json.loads(clean)
    except Exception:
        json_match = re.search(r'\{.*\}', clean, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group())
            except Exception:
                return default_response()
        return default_response()


# -------------------- GET WEATHER --------------------
def get_weather(city="Kathmandu"):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": OPENWEATHER_KEY,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code == 200:
            return {
                "weather": data['weather'][0]['main'],
                "temperature": data['main']['temp'],
                "humidity": data['main']['humidity'],
                "description": data['weather'][0]['description'],
                "success": True
            }
        return get_default_weather()
    except Exception:
        return get_default_weather()


def get_default_weather():
    return {
        "weather": "Clear",
        "temperature": 25,
        "humidity": 60,
        "description": "clear sky",
        "success": False
    }


# -------------------- GET AI RECOMMENDATIONS --------------------
def get_farming_advice(
    disease_name, crop_type, weather, severity
):
    prompt = f"""You are an expert agricultural advisor
for Nepali farmers.

Disease: {disease_name}
Crop: {crop_type}
Current Weather: {weather['weather']},
{weather['temperature']}°C,
Humidity: {weather['humidity']}%
Severity: {severity}

Respond ONLY in JSON:
{{
  "urgency": "Immediate/Within 24 hours/Within a week",
  "weather_impact": "how current weather affects disease",
  "top_advice": [
    "advice 1",
    "advice 2",
    "advice 3"
  ],
  "nepali_advice": [
    "सल्लाह १",
    "सल्लाह २",
    "सल्लाह ३"
  ],
  "nearby_help": "where to get help in Nepal",
  "cost_estimate": "estimated treatment cost in NPR",
  "recovery_time": "expected recovery time"
}}"""

    payload = {
        "model": "llama-3.3-70b-versatile",
        "max_tokens": 800,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    text = call_groq(payload)
    clean = text.replace(
        "```json", "").replace("```", "").strip()

    try:
        return json.loads(clean)
    except Exception:
        return {
            "urgency": "Within a week",
            "weather_impact": "Monitor weather conditions",
            "top_advice": [
                "Consult local agricultural office",
                "Monitor the crop regularly",
                "Apply appropriate treatment"
            ],
            "nepali_advice": [
                "स्थानीय कृषि कार्यालयसँग सल्लाह लिनुस्",
                "बाली नियमित निरीक्षण गर्नुस्",
                "उचित उपचार लागू गर्नुस्"
            ],
            "nearby_help": "Contact local agricultural office",
            "cost_estimate": "NPR 500-2000",
            "recovery_time": "1-2 weeks"
        }


# -------------------- FIND NEARBY OFFICES --------------------
def get_nearby_offices(district="Kathmandu"):
    offices = {
        "Kathmandu": [
            {
                "name": "Department of Agriculture",
                "address": "Harihar Bhawan, Lalitpur",
                "phone": "01-5523963",
                "type": "Government"
            },
            {
                "name": "Agriculture Knowledge Center",
                "address": "Kathmandu",
                "phone": "01-4268177",
                "type": "Government"
            }
        ],
        "default": [
            {
                "name": "District Agriculture Office",
                "address": "Your district headquarters",
                "phone": "Contact local government",
                "type": "Government"
            },
            {
                "name": "Agriculture Service Center",
                "address": "Nearest municipality",
                "phone": "Contact municipality",
                "type": "Government"
            }
        ]
    }
    return offices.get(district, offices["default"])


# -------------------- MAIN ROUTE --------------------
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        image_data = data.get("image")
        city = data.get("city", "Kathmandu")
        language = data.get("language", "english")

        if not image_data:
            return jsonify(
                {"error": "No image provided"}
            ), 400

        # Remove base64 header
        if "," in image_data:
            image_data = image_data.split(",")[1]

        # Convert image to JPEG
        img_bytes = base64.b64decode(image_data)
        img = Image.open(io.BytesIO(img_bytes))
        img = img.convert("RGB")
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=85)
        buffer.seek(0)
        image_data = base64.b64encode(
            buffer.read()
        ).decode("utf-8")

        # Analyze crop image
        analysis = analyze_crop_image(image_data)

        # Get disease info
        disease_info = get_disease_info(
            analysis.get("disease_detected", "")
        )

        # Get severity level
        severity_info = get_severity_level(
            analysis.get("severity", "Low")
        )

        # Get weather
        weather = get_weather(city)

        # Get farming advice
        advice = get_farming_advice(
            analysis.get("disease_detected", "Unknown"),
            analysis.get("crop_type", "Unknown"),
            weather,
            analysis.get("severity", "Low")
        )

        # Get nearby offices
        offices = get_nearby_offices(city)

        return jsonify({
            "success": True,
            "analysis": analysis,
            "disease_info": disease_info,
            "severity_info": severity_info,
            "weather": weather,
            "advice": advice,
            "offices": offices,
            "language": language
        })

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500


# -------------------- WEATHER ROUTE --------------------
@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get("city", "Kathmandu")
    return jsonify(get_weather(city))


# -------------------- HEALTH CHECK --------------------
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"})


# -------------------- RUN --------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)