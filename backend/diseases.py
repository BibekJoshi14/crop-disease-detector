# ============================================
# CROP DISEASE DATABASE FOR NEPAL
# ============================================

CROP_DISEASES = {
    # TOMATO DISEASES
    "Tomato Late Blight": {
        "crop": "Tomato",
        "nepali_name": "टमाटर ढुसी रोग",
        "severity": "High",
        "symptoms": [
            "Dark brown spots on leaves",
            "White fuzzy growth under leaves",
            "Fruits turn brown and rot",
            "Stems turn black"
        ],
        "causes": "Fungal infection by Phytophthora infestans",
        "treatment": [
            "Remove and destroy infected plants",
            "Apply copper-based fungicide",
            "Avoid overhead watering",
            "Improve air circulation"
        ],
        "nepali_treatment": [
            "संक्रमित बिरुवाहरू हटाउनुस्",
            "तामाको आधारित ढुसीनाशक छर्कनुस्",
            "माथिबाट पानी नहाल्नुस्",
            "हावा आवत जावत राम्रो बनाउनुस्"
        ],
        "prevention": "Use resistant varieties, crop rotation",
        "affected_season": "Monsoon (June-September)",
        "estimated_loss": "Up to 100% if untreated",
        "image_signs": "dark brown irregular spots, white mold"
    },

    "Tomato Early Blight": {
        "crop": "Tomato",
        "nepali_name": "टमाटर अगाडि ढुसी",
        "severity": "Medium",
        "symptoms": [
            "Brown spots with rings like a target",
            "Yellow area around spots",
            "Lower leaves affected first",
            "Fruit develops dark leathery spots"
        ],
        "causes": "Fungal infection by Alternaria solani",
        "treatment": [
            "Apply chlorothalonil fungicide",
            "Remove infected leaves",
            "Mulch around plants",
            "Avoid wetting leaves"
        ],
        "nepali_treatment": [
            "क्लोरोथालोनिल ढुसीनाशक छर्कनुस्",
            "संक्रमित पातहरू हटाउनुस्",
            "बिरुवा वरिपरि मल्च गर्नुस्",
            "पात भिज्न नदिनुस्"
        ],
        "prevention": "Proper spacing, avoid overhead irrigation",
        "affected_season": "Late monsoon (August-October)",
        "estimated_loss": "Up to 50% if untreated",
        "image_signs": "concentric ring spots, yellowing leaves"
    },

    # POTATO DISEASES
    "Potato Late Blight": {
        "crop": "Potato",
        "nepali_name": "आलु ढुसी रोग",
        "severity": "High",
        "symptoms": [
            "Water soaked spots on leaves",
            "White mold on leaf undersides",
            "Tubers develop reddish brown rot",
            "Entire plant collapses quickly"
        ],
        "causes": "Fungal infection by Phytophthora infestans",
        "treatment": [
            "Apply metalaxyl fungicide immediately",
            "Remove infected plants",
            "Harvest tubers early if disease spreads",
            "Do not store infected tubers"
        ],
        "nepali_treatment": [
            "तुरुन्त मेटालाक्सिल ढुसीनाशक छर्कनुस्",
            "संक्रमित बिरुवाहरू हटाउनुस्",
            "रोग फैलिए आलु चाँडो उखेल्नुस्",
            "संक्रमित आलु भण्डार नगर्नुस्"
        ],
        "prevention": "Use certified disease-free seeds",
        "affected_season": "Monsoon (June-September)",
        "estimated_loss": "Up to 80% if untreated",
        "image_signs": "water soaked lesions, white cottony growth"
    },

    "Potato Black Scurf": {
        "crop": "Potato",
        "nepali_name": "आलु कालो खुर्पे",
        "severity": "Medium",
        "symptoms": [
            "Black crusty patches on tubers",
            "Stunted plant growth",
            "Distorted stems near soil",
            "Reduced tuber size"
        ],
        "causes": "Fungal infection by Rhizoctonia solani",
        "treatment": [
            "Use fungicide treated seed tubers",
            "Plant in warm well drained soil",
            "Avoid deep planting",
            "Rotate crops annually"
        ],
        "nepali_treatment": [
            "ढुसीनाशकले उपचार गरिएको बीउ प्रयोग गर्नुस्",
            "न्यानो र राम्रो निकास भएको माटोमा रोप्नुस्",
            "धेरै गहिरो नरोप्नुस्",
            "वार्षिक बाली चक्र अपनाउनुस्"
        ],
        "prevention": "Crop rotation, certified seed potatoes",
        "affected_season": "Year round",
        "estimated_loss": "Up to 30% if untreated",
        "image_signs": "black sclerotia on tuber surface"
    },

    # RICE DISEASES
    "Rice Blast": {
        "crop": "Rice",
        "nepali_name": "धान ब्लास्ट रोग",
        "severity": "High",
        "symptoms": [
            "Diamond shaped spots on leaves",
            "Gray center with brown border",
            "Neck of panicle turns black",
            "Grains become unfilled"
        ],
        "causes": "Fungal infection by Magnaporthe oryzae",
        "treatment": [
            "Apply tricyclazole fungicide",
            "Use resistant rice varieties",
            "Balanced fertilizer application",
            "Avoid excess nitrogen"
        ],
        "nepali_treatment": [
            "ट्राइसाइक्लाजोल ढुसीनाशक छर्कनुस्",
            "रोग प्रतिरोधी धानको जात प्रयोग गर्नुस्",
            "सन्तुलित मल प्रयोग गर्नुस्",
            "अत्यधिक नाइट्रोजन नहाल्नुस्"
        ],
        "prevention": "Silicon fertilizer, balanced nutrition",
        "affected_season": "Monsoon (June-September)",
        "estimated_loss": "Up to 70% if untreated",
        "image_signs": "diamond shaped lesions, neck rot"
    },

    "Rice Brown Spot": {
        "crop": "Rice",
        "nepali_name": "धान खैरो दाग",
        "severity": "Medium",
        "symptoms": [
            "Brown oval spots on leaves",
            "Spots have yellow halo",
            "Infected grains turn brown",
            "Seedling blight in nursery"
        ],
        "causes": "Fungal infection by Bipolaris oryzae",
        "treatment": [
            "Apply mancozeb fungicide",
            "Seed treatment before planting",
            "Balanced potassium fertilizer",
            "Remove infected plant debris"
        ],
        "nepali_treatment": [
            "म्यानकोजेब ढुसीनाशक छर्कनुस्",
            "रोप्नु अघि बीउ उपचार गर्नुस्",
            "सन्तुलित पोटासियम मल हाल्नुस्",
            "संक्रमित बिरुवाको अवशेष हटाउनुस्"
        ],
        "prevention": "Balanced fertilization, seed treatment",
        "affected_season": "Late monsoon",
        "estimated_loss": "Up to 45% if untreated",
        "image_signs": "oval brown spots with yellow halo"
    },

    # WHEAT DISEASES
    "Wheat Rust": {
        "crop": "Wheat",
        "nepali_name": "गहुँ खिया रोग",
        "severity": "High",
        "symptoms": [
            "Orange red pustules on leaves",
            "Pustules on stems and heads",
            "Leaves turn yellow and dry",
            "Reduced grain filling"
        ],
        "causes": "Fungal infection by Puccinia species",
        "treatment": [
            "Apply propiconazole fungicide",
            "Use rust resistant varieties",
            "Early planting to avoid peak rust",
            "Monitor fields regularly"
        ],
        "nepali_treatment": [
            "प्रोपिकोनाजोल ढुसीनाशक छर्कनुस्",
            "खिया प्रतिरोधी गहुँको जात प्रयोग गर्नुस्",
            "खिया चरम बेला भन्दा अगाडि रोप्नुस्",
            "खेत नियमित निरीक्षण गर्नुस्"
        ],
        "prevention": "Resistant varieties, early planting",
        "affected_season": "Winter (November-March)",
        "estimated_loss": "Up to 60% if untreated",
        "image_signs": "orange pustules on leaves and stems"
    },

    # MAIZE DISEASES
    "Maize Northern Leaf Blight": {
        "crop": "Maize",
        "nepali_name": "मकै पात ढुसी",
        "severity": "Medium",
        "symptoms": [
            "Long gray green lesions on leaves",
            "Lesions turn tan with wavy edges",
            "Lower leaves affected first",
            "Severe cases affect entire plant"
        ],
        "causes": "Fungal infection by Exserohilum turcicum",
        "treatment": [
            "Apply azoxystrobin fungicide",
            "Plant resistant hybrids",
            "Crop rotation with non-host crops",
            "Remove crop debris after harvest"
        ],
        "nepali_treatment": [
            "एजोक्सिस्ट्रोबिन ढुसीनाशक छर्कनुस्",
            "रोग प्रतिरोधी संकर जात रोप्नुस्",
            "गैर-पोषक बालीसँग बाली चक्र गर्नुस्",
            "कटानपछि बाली अवशेष हटाउनुस्"
        ],
        "prevention": "Resistant varieties, crop rotation",
        "affected_season": "Monsoon (June-September)",
        "estimated_loss": "Up to 40% if untreated",
        "image_signs": "long cigar shaped gray lesions"
    },

    # GENERAL
    "Healthy Crop": {
        "crop": "General",
        "nepali_name": "स्वस्थ बाली",
        "severity": "None",
        "symptoms": ["No disease symptoms detected"],
        "causes": "No disease",
        "treatment": ["Continue regular maintenance"],
        "nepali_treatment": ["नियमित हेरचाह जारी राख्नुस्"],
        "prevention": "Regular monitoring and good agricultural practices",
        "affected_season": "N/A",
        "estimated_loss": "None",
        "image_signs": "healthy green leaves"
    }
}


def get_disease_info(disease_name):
    """Get disease information from database"""
    for key in CROP_DISEASES:
        if key.lower() in disease_name.lower() or \
           disease_name.lower() in key.lower():
            return CROP_DISEASES[key]
    return CROP_DISEASES["Healthy Crop"]


def get_all_diseases():
    """Get list of all diseases"""
    return list(CROP_DISEASES.keys())


def get_diseases_by_crop(crop_name):
    """Get all diseases for a specific crop"""
    return {
        k: v for k, v in CROP_DISEASES.items()
        if v['crop'].lower() == crop_name.lower()
    }


def get_severity_level(severity):
    """Get severity color and emoji"""
    levels = {
        "High": {"color": "#ef4444", "emoji": "🔴"},
        "Medium": {"color": "#f59e0b", "emoji": "🟡"},
        "Low": {"color": "#22c55e", "emoji": "🟢"},
        "None": {"color": "#22c55e", "emoji": "✅"}
    }
    return levels.get(severity, levels["Low"])