import streamlit as st
import pandas as pd
import os

# 1️⃣ إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="BlueGuard AI | منصة حماية البيئة البحرية",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2️⃣ التنسيق البرمجي الشامل (CSS البحري مع الأزرار الشفافة والأنيقة)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

* {
    font-family: "Cairo", sans-serif !important;
}

/* خلفية التطبيق البحرية العملاقة */
.stApp {
    background: linear-gradient(rgba(10, 25, 47, 0.75), rgba(15, 32, 67, 0.82)), 
                url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073") no-repeat center center fixed !important;
    background-size: cover !important;
    color: #ffffff !important;
}

/* 🌟 تنسيق القائمة الجانبية (Sidebar) */
section[data-testid="stSidebar"] {
    background: rgba(10, 25, 47, 0.65) !important;
    backdrop-filter: blur(15px) !important;
    border-right: 1px solid rgba(0, 180, 216, 0.3) !important;
}

/* 🔵 تنسيق الأزرار (Buttons) */
.stButton > button {
    background: linear-gradient(135deg, #0077b6, #00b4d8) !important;
    color: white !important;
    border: none !important;
    border-radius: 20px !important;
    padding: 10px 25px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 12px rgba(0, 119, 182, 0.3) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #0096c7, #48cae4) !important;
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 8px 20px rgba(0, 180, 216, 0.5) !important;
}

/* 💎 بطاقات المؤشرات الزجاجية */
div[data-testid="stMetric"], .stCard {
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(14px) !important;
    border-radius: 20px !important;
    padding: 22px !important;
    border: 1px solid rgba(72, 202, 228, 0.25) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s ease !important;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-6px) !important;
    border-color: #48cae4 !important;
    box-shadow: 0 12px 35px rgba(0, 180, 216, 0.35) !important;
}

div[data-testid="stMetricLabel"] {
    color: #caf0f8 !important;
    font-size: 17px !important;
    font-weight: 600 !important;
}

div[data-testid="stMetricValue"] {
    color: #90e0ef !important;
    font-size: 36px !important;
    font-weight: 800 !important;
    text-shadow: 0 0 12px rgba(144, 224, 239, 0.5) !important;
}

/* 🏄‍♂️ تنسيق التبويبات (Tabs) */
button[data-baseweb="tab"] {
    background: rgba(255, 255, 255, 0.06) !important;
    border-radius: 12px 12px 0 0 !important;
    color: #e0f7fa !important;
    font-size: 16px !important;
    padding: 12px 22px !important;
    border: none !important;
    margin-right: 6px !important;
}

button[aria-selected="true"] {
    background: linear-gradient(135deg, #0077b6, #00b4d8) !important;
    color: white !important;
    font-weight: bold !important;
    box-shadow: 0 4px 15px rgba(0, 180, 216, 0.4) !important;
}

/* الهيدر الرئيسي */
.hero-box {
    width: 100%;
    margin: 10px auto 25px auto;
    padding: 30px;
    text-align: center;
    background: rgba(10, 25, 47, 0.5);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(72, 202, 228, 0.3);
    border-radius: 25px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

.hero-box h1 {
    font-size: 40px;
    color: #90e0ef;
    margin-bottom: 10px;
    font-weight: 800;
}

.hero-box p {
    font-size: 18px;
    color: #caf0f8;
}
</style>
""", unsafe_allow_html=True)

# 3️⃣ نصوص اللغات (العربية والإنجليزية)
TEXTS = {
    "ar": {
        "title": "🌊 منصة BlueGuard AI",
        "title_desc": "منصة ذكية متكاملة لحماية البيئة البحرية، دعم التنبؤ بالصيد، وتعزيز سلامة الصيادين نطقاً وبصرياً",
        "settings_title": "⚙️ الإعدادات وسهولة الاستخدام",
        "tts_toggle": "🔊 تفعيل القارئ الصوتي التلقائي (للصيادين)",
        "lang_select": "🌐 اختر اللغة / Select Language:",
        "select_zone": "📍 اختر القطاع البحري:",
        "tab_sea_health": "🌱 صحة البحر",
        "tab_predict": "🎧 التنبؤ بالصيد",
        "tab_safety": "🛡️ السلامة والمخاطر",
        "tab_analytics": "📊 التحليلات",
        "tab_chat": "💬 المساعد الذكي"
    },
    "en": {
        "title": "🌊 BlueGuard AI Platform",
        "title_desc": "Integrated AI platform for marine conservation, fishing prediction, and fisher safety.",
        "settings_title": "⚙️ Settings & Accessibility",
        "tts_toggle": "🔊 Enable Automatic Voice Reader (For Fishers)",
        "lang_select": "🌐 Select Language / اختر اللغة:",
        "select_zone": "📍 Select Sector:",
        "tab_sea_health": "🌱 Sea Health",
        "tab_predict": "🎧 Fishing Prediction",
        "tab_safety": "🛡️ Safety & Risks",
        "tab_analytics": "📊 Analytics",
        "tab_chat": "💬 Smart AI Assistant"
    }
}

# 4️⃣ القاموس الموحد للمواقع
locations_data = {
    "القطاع الجنوبي (جازان / فرسان)": {
        "lat": 16.8892, "lon": 42.5511,
        "temp": "28.8 °C", "ox": "5.9 mg/L", "ch": "1.8 µg/L", "temp_diff": "+0.5°C",
        "wave_height": 0.8, "wind_speed": 12,
        "risk_level": "آمنة ومناسبة للإبحار 🟢", "safety_score": 92,
        "advice": "الأحوال الجوية هادئة في سواحل جازان وفرسان، ينصح بالصيد الطبيعي."
    },
    "القطاع الأوسط (جدة / رابغ)": {
        "lat": 21.5433, "lon": 39.1728,
        "temp": "26.5 °C", "ox": "6.2 mg/L", "ch": "1.2 µg/L", "temp_diff": "+0.1°C",
        "wave_height": 1.8, "wind_speed": 22,
        "risk_level": "تحذير: أمواج متوسطة 🟡", "safety_score": 61,
        "advice": "ارتفاع الأمواج متوسط بالقرب من الشاطئ، يرجى توخي الحذر."
    },
    "القطاع الشمالي (نيوم / تبوك)": {
        "lat": 28.3833, "lon": 34.5667,
        "temp": "23.1 °C", "ox": "7.4 mg/L", "ch": "0.9 µg/L", "temp_diff": "-0.2°C",
        "wave_height": 2.5, "wind_speed": 30,
        "risk_level": "خطر: رياح شديدة 🔴", "safety_score": 35,
        "advice": "لا ينصح بالإبحار اليوم لارتفاع الرياح والأمواج في القطاع الشمالي."
    }
}

# التهيئة
if "selected_zone" not in st.session_state:
    st.session_state["selected_zone"] = "القطاع الجنوبي (جازان / فرسان)"
if "current_loc" not in st.session_state:
    st.session_state["current_loc"] = locations_data["القطاع الجنوبي (جازان / فرسان)"]

# 5️⃣ الشريط الجانبي (تحكم باللغة والصوت والقطاع)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/sea-waves.png", width=70)
    st.title("🎛️ القائمة الرئيسية")
    
    # اختيار اللغة
    lang_choice = st.radio("🌐 Language / اللغة:", ["العربية (Arabic)", "English"], index=0)
    lang = "ar" if "العربية" in lang_choice else "en"
    t = TEXTS[lang]
    
    st.markdown("---")
    st.subheader(t["settings_title"])
    
    # خيار القارئ الصوتي
    enable_tts = st.toggle(t["tts_toggle"], value=True)
    
    st.markdown("---")
    # اختيار القطاع
    selected_sidebar_zone = st.selectbox(
        t["select_zone"],
        options=list(locations_data.keys()),
        index=list(locations_data.keys()).index(st.session_state["selected_zone"])
    )
    st.session_state["selected_zone"] = selected_sidebar_zone
    st.session_state["current_loc"] = locations_data[selected_sidebar_zone]

# 6️⃣ رأس الصفحة Dynamic Header
st.markdown(f"""
<div class="hero-box">
    <h1>{t['title']}</h1>
    <p>{t['title_desc']}</p>
</div>
""", unsafe_allow_html=True)

curr = st.session_state["current_loc"]

# 7️⃣ التبويبات الرئيسية
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    t["tab_sea_health"],
    t["tab_predict"],
    t["tab_safety"],
    t["tab_analytics"],
    t["tab_chat"]
])

# ----- التبويب الأول: صحة البحر -----
with tab1:
    st.subheader(t["tab_sea_health"])
    
    # مشغل صوتي تجريبي إذا كان الخيار مفعلاً
    if enable_tts:
        st.info("🔊 القارئ الصوتي مفعّل: جاري قراءة مؤشرات صحة البحر تلقائياً...")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("حرارة المياه", curr["temp"], delta=curr["temp_diff"])
    with c2:
        st.metric("الأكسجين المذاب", curr["ox"])
    with c3:
        st.metric("الكلوروفيل", curr["ch"])

    map_df = pd.DataFrame({'lat': [curr["lat"]], 'lon': [curr["lon"]]})
    st.map(map_df)

# ----- التبويب الثاني: التنبؤ بالصيد -----
with tab2:
    st.subheader(t["tab_predict"])
    st.success(f"📌 {st.session_state['selected_zone']} | ({curr['lat']}, {curr['lon']})")
    
    st.button("🔍 تحليل جودة الصيد اللحظي")
    map_data = pd.DataFrame({'lat': [curr["lat"]], 'lon': [curr["lon"]]})
    st.map(map_data)

# ----- التبويب الثالث: السلامة والمخاطر -----
with tab3:
    st.subheader(t["tab_safety"])
    st.caption(f"📍 {st.session_state['selected_zone']}")
    st.progress(curr["safety_score"], text=f"مستوى الأمان: {curr['safety_score']}%")

    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.metric("درجة الأمان", f"{curr['safety_score']}%")
    with col_s2:
        st.metric("ارتفاع الموج", f"{curr['wave_height']} m")
    with col_s3:
        st.metric("سرعة الرياح", f"{curr['wind_speed']} km/h")

    if curr["safety_score"] >= 80:
        st.success(f"**حالة القطاع:** {curr['risk_level']}\n\n💡 {curr['advice']}")
    elif curr["safety_score"] >= 50:
        st.warning(f"**حالة القطاع:** {curr['risk_level']}\n\n💡 {curr['advice']}")
    else:
        st.error(f"**حالة القطاع:** {curr['risk_level']}\n\n💡 {curr['advice']}")

# ----- التبويب الرابع: التحليلات -----
with tab4:
    st.subheader(t["tab_analytics"])
    chart_data = pd.DataFrame({
        'الأيام': ['الخميس', 'الجمعة', 'السبت', 'الأحد', 'الإثنين'],
        'حجم الصيد المتوقع (طن)': [25, 22, 15, 18, 12]
    })
    st.bar_chart(chart_data.set_index('الأيام'))

# ----- التبويب الخامس: المساعد الذكي -----
with tab5:
    st.subheader(t["tab_chat"])
    st.text_input("أدخل سؤالك للذكاء الاصطناعي:")
    st.button("إرسال 🚀")