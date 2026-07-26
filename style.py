@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

/* تطبيق خط القاهرة للواجهة بالكامل */
* {
    font-family: "Cairo", sans-serif !important;
}

/* خلفية الموقع البحرية */
.stApp {
    background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), 
                url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073") no-repeat center center fixed !important;
    background-size: cover !important;
    color: white !important;
}

/* تصميم البطاقات الزجاجية (Glassmorphism) */
div[data-testid="stMetric"], .stCard, div[data-testid="stVerticalBlock"] > div[style*="background"] {
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border-radius: 20px !important;
    padding: 25px !important;
    border: 1px solid rgba(255, 255, 255, 0.25) !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25) !important;
    transition: transform 0.3s ease, background 0.3s ease !important;
}

/* تأثير تحريك البطاقات عند مرور الماوس */
div[data-testid="stMetric"]:hover {
    transform: translateY(-8px) !important;
    background: rgba(255, 255, 255, 0.2) !important;
}

/* ألوان العناوين والأرقام داخل البطاقات */
div[data-testid="stMetricLabel"] {
    color: #ffffff !important;
    font-size: 17px !important;
    font-weight: 600 !important;
}

div[data-testid="stMetricValue"] {
    color: #4ecbff !important;
    font-size: 38px !important;
    font-weight: 800 !important;
    text-shadow: 0 0 10px rgba(78, 203, 255, 0.5) !important;
}

/* تنسيق التبويبات العلويّة (Tabs) */
button[data-baseweb="tab"] {
    background: rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px 12px 0 0 !important;
    color: white !important;
    font-size: 16px !important;
    padding: 12px 24px !important;
    border: none !important;
    margin-right: 6px !important;
    backdrop-filter: blur(10px) !important;
}

button[aria-selected="true"] {
    background: #00b8ff !important;
    color: white !important;
    font-weight: bold !important;
    box-shadow: 0 4px 15px rgba(0, 184, 255, 0.4) !important;
}

/* القوائم المنسدلة */
div[data-baseweb="select"] > div {
    background: rgba(0, 0, 0, 0.4) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    color: white !important;
}