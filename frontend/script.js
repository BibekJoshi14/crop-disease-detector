// ============================================
// KISAAN SAHAYAK — Crop Disease Detector
// ============================================

const BACKEND_URL = 'https://crop-disease-detector-nu.vercel.app';

// State
let currentAnalysis = null;
let totalScans = 0;
let diseasesFound = 0;
let healthyFound = 0;
let currentLanguage = 'english';

// ============================================
// TRANSLATIONS
// ============================================
const translations = {
  english: {
    uploadText: 'Click to upload crop photo',
    uploadHint: 'Take a clear photo of the affected leaves or plant',
    analyzeBtnText: 'Analyze Crop',
    loadingText: '🤖 AI is analyzing your crop...',
    symptomsTitle: '🔍 Symptoms Detected',
    treatmentTitle: '💊 Treatment',
    adviceTitle: '🤖 AI Recommendations',
    guideTitle: '📖 How to Use',
    cropsTitle: '🌱 Supported Crops',
    tipsTitle: '💡 Farming Tips',
    step1: 'Take a clear photo of the affected crop',
    step2: 'Upload the photo by clicking the camera icon',
    step3: 'Click Analyze Crop and wait for AI analysis',
    step4: 'Follow the treatment recommendations',
  },
  nepali: {
    uploadText: 'बाली फोटो अपलोड गर्न क्लिक गर्नुस्',
    uploadHint: 'प्रभावित पात वा बिरुवाको स्पष्ट फोटो खिच्नुस्',
    analyzeBtnText: 'बाली विश्लेषण गर्नुस्',
    loadingText: '🤖 AI ले तपाईंको बाली विश्लेषण गर्दैछ...',
    symptomsTitle: '🔍 देखिएका लक्षणहरू',
    treatmentTitle: '💊 उपचार',
    adviceTitle: '🤖 AI सल्लाह',
    guideTitle: '📖 कसरी प्रयोग गर्ने',
    cropsTitle: '🌱 समर्थित बालीहरू',
    tipsTitle: '💡 खेती सुझावहरू',
    step1: 'प्रभावित बालीको स्पष्ट फोटो खिच्नुस्',
    step2: 'क्यामेरा आइकनमा क्लिक गरेर फोटो अपलोड गर्नुस्',
    step3: 'बाली विश्लेषण गर्नुस् क्लिक गरेर AI विश्लेषणको प्रतीक्षा गर्नुस्',
    step4: 'उपचार सिफारिसहरू पालना गर्नुस्',
  }
};

// ============================================
// LANGUAGE CHANGE
// ============================================
function changeLanguage() {
  currentLanguage = document.getElementById(
    'languageSelect'
  ).value;
  const t = translations[currentLanguage];

  document.getElementById('uploadText').textContent =
    t.uploadText;
  document.getElementById('uploadHint').textContent =
    t.uploadHint;
  document.getElementById('analyzeBtnText').textContent =
    t.analyzeBtnText;
  document.getElementById('loadingText').textContent =
    t.loadingText;
  document.getElementById('symptomsTitle').textContent =
    t.symptomsTitle;
  document.getElementById('treatmentTitle').textContent =
    t.treatmentTitle;
  document.getElementById('adviceTitle').textContent =
    t.adviceTitle;
  document.getElementById('guideTitle').textContent =
    t.guideTitle;
  document.getElementById('cropsTitle').textContent =
    t.cropsTitle;
  document.getElementById('tipsTitle').textContent =
    t.tipsTitle;
  document.getElementById('step1').textContent = t.step1;
  document.getElementById('step2').textContent = t.step2;
  document.getElementById('step3').textContent = t.step3;
  document.getElementById('step4').textContent = t.step4;
}

// ============================================
// IMAGE UPLOAD
// ============================================
function handleUpload(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = (e) => {
    document.getElementById('cropPreview').src =
      e.target.result;
    document.getElementById('uploadBox').classList
      .add('hidden');
    document.getElementById('previewBox').classList
      .remove('hidden');
    document.getElementById('results').classList
      .add('hidden');
  };
  reader.readAsDataURL(file);
}

// Drag and drop
const uploadBox = document.getElementById('uploadBox');

uploadBox.addEventListener('dragover', (e) => {
  e.preventDefault();
  uploadBox.style.borderColor = '#2d6a2d';
  uploadBox.style.background = '#f0fff0';
});

uploadBox.addEventListener('dragleave', () => {
  uploadBox.style.borderColor = '#4caf50';
  uploadBox.style.background = '#f9fff9';
});

uploadBox.addEventListener('drop', (e) => {
  e.preventDefault();
  uploadBox.style.borderColor = '#4caf50';
  const file = e.dataTransfer.files[0];
  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = (ev) => {
      document.getElementById('cropPreview').src =
        ev.target.result;
      document.getElementById('uploadBox').classList
        .add('hidden');
      document.getElementById('previewBox').classList
        .remove('hidden');
    };
    reader.readAsDataURL(file);
  }
});

// Clear image
function clearImage() {
  document.getElementById('cropPreview').src = '';
  document.getElementById('fileInput').value = '';
  document.getElementById('uploadBox').classList
    .remove('hidden');
  document.getElementById('previewBox').classList
    .add('hidden');
  document.getElementById('results').classList
    .add('hidden');
  document.getElementById('loading').classList
    .add('hidden');
}

// ============================================
// ANALYZE CROP
// ============================================
async function analyzeCrop() {
  const preview = document.getElementById('cropPreview');
  if (!preview.src ||
    preview.src === window.location.href) {
    alert('Please upload a crop photo first!');
    return;
  }

  const city = document.getElementById('citySelect').value;

  // Show loading
  document.getElementById('loading').classList
    .remove('hidden');
  document.getElementById('results').classList
    .add('hidden');
  document.getElementById('analyzeBtn').disabled = true;

  try {
    const response = await fetch(
      `${BACKEND_URL}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          image: preview.src,
          city: city,
          language: currentLanguage
        })
      }
    );

    const data = await response.json();

    if (!data.success) {
      throw new Error(data.error || 'Analysis failed');
    }

    currentAnalysis = data;
    totalScans++;

    if (data.analysis.disease_detected === 'Healthy Crop'
      || data.analysis.severity === 'None') {
      healthyFound++;
    } else {
      diseasesFound++;
    }

    updateSessionStats();
    renderResults(data);

  } catch (err) {
    alert('Analysis failed: ' + err.message);
    console.error(err);
  } finally {
    document.getElementById('loading').classList
      .add('hidden');
    document.getElementById('analyzeBtn').disabled = false;
  }
}

// ============================================
// RENDER RESULTS
// ============================================
function renderResults(data) {
  document.getElementById('results').classList
    .remove('hidden');

  const analysis = data.analysis;
  const diseaseInfo = data.disease_info;
  const advice = data.advice;
  const severityInfo = data.severity_info;

  // Disease name
  document.getElementById('diseaseName').textContent =
    analysis.disease_detected || 'Unknown';

  // Nepali name
  document.getElementById('diseaseNepali').textContent =
    diseaseInfo.nepali_name || '';

  // Severity badge
  const badge = document.getElementById('severityBadge');
  badge.textContent = analysis.severity || 'LOW';
  badge.style.background = severityInfo.color || '#22c55e';

  // Stats
  document.getElementById('confidence').textContent =
    (analysis.confidence || 0) + '%';
  document.getElementById('affectedArea').textContent =
    (analysis.affected_area_percent || 0) + '%';
  document.getElementById('cropType').textContent =
    analysis.crop_type || '--';

  // Immediate action
  document.getElementById('immediateAction').innerHTML =
    `⚡ <strong>Immediate Action:</strong>
    ${analysis.immediate_action ||
    'Monitor the crop closely'}`;

  // Symptoms
  const symptoms = analysis.visible_symptoms ||
    diseaseInfo.symptoms || [];
  document.getElementById('symptomsList').innerHTML =
    symptoms.map(s => `<li>${s}</li>`).join('');

  // Treatment
  const treatment = currentLanguage === 'nepali'
    ? diseaseInfo.nepali_treatment
    : diseaseInfo.treatment || [];
  document.getElementById('treatmentList').innerHTML =
    treatment.map(t => `<li>${t}</li>`).join('');

  // AI Advice
  const adviceList = currentLanguage === 'nepali'
    ? advice.nepali_advice
    : advice.top_advice || [];
  document.getElementById('adviceList').innerHTML =
    adviceList.map(a => `<li>${a}</li>`).join('');

  // Urgency badge
  const urgencyBadge =
    document.getElementById('urgencyBadge');
  urgencyBadge.textContent = advice.urgency || 'Normal';
  urgencyBadge.style.background =
    advice.urgency === 'Immediate' ? '#ef4444' :
    advice.urgency === 'Within 24 hours' ? '#f59e0b' :
    '#22c55e';

  // Recovery and cost
  document.getElementById('recoveryTime').textContent =
    '⏱️ Recovery: ' +
    (advice.recovery_time || 'Unknown');
  document.getElementById('costEstimate').textContent =
    '💰 Cost: ' +
    (advice.cost_estimate || 'Unknown');

  // Weather impact
  document.getElementById('weatherImpactText')
    .textContent = advice.weather_impact ||
    'No specific weather impact detected';

  // Offices
  const offices = data.offices || [];
  document.getElementById('officesList').innerHTML =
    offices.map(o => `
      <div class="office-item">
        <div class="office-name">🏢 ${o.name}</div>
        <div class="office-address">📍 ${o.address}</div>
        <div class="office-phone">📞 ${o.phone}</div>
      </div>
    `).join('');
}

// ============================================
// UPDATE SESSION STATS
// ============================================
function updateSessionStats() {
  document.getElementById('totalScans').textContent =
    totalScans;
  document.getElementById('diseasesFound').textContent =
    diseasesFound;
  document.getElementById('healthyFound').textContent =
    healthyFound;
}

// ============================================
// WEATHER
// ============================================
async function updateWeather() {
  const city =
    document.getElementById('citySelect').value;
  document.getElementById('cityText').textContent = city;

  try {
    const response = await fetch(
      `${BACKEND_URL}/weather?city=${city}`
    );
    const data = await response.json();

    if (data.success !== false) {
      const icons = {
        'Clear': '☀️',
        'Clouds': '☁️',
        'Rain': '🌧️',
        'Drizzle': '🌦️',
        'Thunderstorm': '⛈️',
        'Snow': '❄️',
        'Mist': '🌫️'
      };

      document.getElementById('weatherIcon')
        .textContent = icons[data.weather] || '🌤️';
      document.getElementById('weatherText')
        .textContent = data.description;
      document.getElementById('tempText')
        .textContent = data.temperature + '°C';
      document.getElementById('humidityText')
        .textContent = data.humidity + '%';
    }
  } catch (err) {
    console.log('Weather fetch failed:', err);
  }
}

// ============================================
// START
// ============================================
updateWeather();