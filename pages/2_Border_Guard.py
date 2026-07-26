import streamlit as st
import pandas as pd

# 1️⃣ إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="BlueGuard | حرس الحدود والرقابة البحرية",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2️⃣ التنسيق البرمجي الشامل (CSS البحري مع الأزرار والبطاقات الزجاجية)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

* {
    font-family: "Cairo", sans-serif !important;
}

/* خلفية التطبيق البحرية العملاقة */
.stApp {
    background: linear-gradient(rgba(10, 25, 47, 0.78), rgba(15, 32, 67, 0.85)), 
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

/* 💎 بطاقات المؤشرات والتنبيهات الزجاجية */
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

# 3️⃣ نصوص اللغات (العربية والإنجليزية) الخاصة بصفحة حرس الحدود
TEXTS = {
    "ar": {
        "title": "🛡️ بوابـة حـرس الحـدود والرقابـة الميدانيـة",
        "title_desc": "منظومة المراقبة والتحليل الذكي لردع الصيد غير القانوني ومتابعة بلاغات السلامة البحرية",
        "settings_title": "⚙️ إعدادات الرقابة والصوت",
        "tts_toggle": "🔊 تفعيل التنبيهات الصوتية الحية",
        "select_sector": "🚨 اختر مركز الرقابة / القطاع:",
        "tab_live_map": "📡 الرقابة المباشرة",
        "tab_ai_detection": "📸 التحليل البصري (AI)",
        "tab_reports": "📋 البلاغات والإنذارات",
        "tab_patrols": "🚤 إدارة دوريات الإنقاذ"
    },
    "en": {
        "title": "🛡️ Border Guard & Maritime Surveillance",
        "title_desc": "AI Monitoring system for detecting illegal fishing and managing marine emergency reports.",
        "settings_title": "⚙️ Surveillance Settings",
        "tts_toggle": "🔊 Enable Live Voice Alerts",
        "select_sector": "🚨 Select Patrol Sector:",
        "tab_live_map": "📡 Live Surveillance",
        "tab_ai_detection": "📸 AI Visual Analysis",
        "tab_reports": "📋 Emergency Reports",
        "tab_patrols": "🚤 Fleet & Patrols"
    }
}

# بيانات قطاعات الرقابة
sectors_data = {
    "قطاع جازان وفرسان (الحدود الجنوبية)": {
        "lat": 16.8892, "lon": 42.5511,
        "active_boats": 14, "alerts_today": 2, "status": "مستقر 🟢"
    },
    "قطاع جدة ورابغ (المنطقة الوسطى)": {
        "lat": 21.5433, "lon": 39.1728,
        "active_boats": 22, "alerts_today": 5, "status": "مراقبة مكثفة 🟡"
    },
    "قطاع نيوم وتبوك (الحدود الشمالية)": {
        "lat": 28.3833, "lon": 34.5667,
        "active_boats": 9, "alerts_today": 1, "status": "مستقر 🟢"
    }
}

if "bg_sector" not in st.session_state:
    st.session_state["bg_sector"] = "قطاع جازان وفرسان (الحدود الجنوبية)"

# 4️⃣ الشريط الجانبي (Sidebar)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/shield.png", width=70)
    st.title("🛡️ غرفة التحكم")
    
    # اختيار اللغة
    lang_choice = st.radio("🌐 Language / اللغة:", ["العربية (Arabic)", "English"], index=0)
    lang = "ar" if "العربية" in lang_choice else "en"
    t = TEXTS[lang]
    
    st.markdown("---")
    st.subheader(t["settings_title"])
    
    # تفعيل الصوت
    enable_tts = st.toggle(t["tts_toggle"], value=True)
    
    st.markdown("---")
    selected_sector = st.selectbox(
        t["select_sector"],
        options=list(sectors_data.keys()),
        index=list(sectors_data.keys()).index(st.session_state["bg_sector"])
    )
    st.session_state["bg_sector"] = selected_sector

# 5️⃣ الهيدر الرئيسي
st.markdown(f"""
<div class="hero-box">
    <h1>{t['title']}</h1>
    <p>{t['title_desc']}</p>
</div>
""", unsafe_allow_html=True)

sec_info = sectors_data[st.session_state["bg_sector"]]

# 6️⃣ التبويبات الرئيسية
tab1, tab2, tab3, tab4 = st.tabs([
    t["tab_live_map"],
    t["tab_ai_detection"],
    t["tab_reports"],
    t["tab_patrols"]
])

# ----- التبويب الأول: الرقابة المباشرة -----
with tab1:
    st.subheader(t["tab_live_map"])
    
    if enable_tts:
        st.info("🔊 القارئ الصوتي مفعّل: التنبيهات المباشرة متصلة بمركز العمليات.")

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("حالة القطاع", sec_info["status"])
    with m2:
        st.metric("قوارب الدورية النشطة", f"{sec_info['active_boats']} قارب")
    with m3:
        st.metric("إنذارات اليوم", f"{sec_info['alerts_today']} بلاغات")

    st.markdown("### 🗺️ خريطة التتبع المباشر للقطع البحرية")
    map_df = pd.DataFrame({'lat': [sec_info["lat"]], 'lon': [sec_info["lon"]]})
    st.map(map_df)

# ----- التبويب الثاني: التحليل البصري للذكاء الاصطناعي -----
with tab2:
    st.subheader(t["tab_ai_detection"])
    st.write("📷 **رفع صورة أو رصد كاميرا لمسرح الجريمة / المخالفة البحرية:**")
    
    uploaded_img = st.file_uploader("قم برفع صورة قارب أو منطقة صيد للتحليل بواسطة الذكاء الاصطناعي:", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_img:
        st.image(uploaded_img, caption="الصورة المرصودة", width=400)
        if st.button("🔍 بدء التحليل والرصد الأمني"):
            st.success("✅ تم التحليل: لا توجد أدوات صيد محظورة (شباك قاعية) متطابقة مع الصورة.")

# ----- التبويب الثالث: البلاغات والإنذارات -----
with tab3:
    st.subheader(t["tab_reports"])
    st.write("📋 **سجل البلاغات البحرية اللحظية:**")
    
    reports_df = pd.DataFrame({
        "رقم البلاغ": ["#1082", "#1083", "#1084"],
        "القطاع": ["جازان", "جدة", "تبوك"],
        "نوع البلاغ": ["دخول منطقة محمية", "طلب استغاثة موج مرتفع", "صيد بدون تصريح"],
        "الحالة": ["تمت الاستجابة 🟢", "قيد المتابعة 🟡", "مغلق ⚪"]
    })
    st.dataframe(reports_df, use_container_width=True)

# ----- التبويب الرابع: إدارة الدوريات -----
with tab4:
    st.subheader(t["tab_patrols"])
    st.write("🚤 **إعادة توزيع ودعم دوريات السلامة:**")
    st.slider("حدد عدد قوارب الإنقاذ المطلوبة للقطاع الحالي:", 1, 30, sec_info["active_boats"])
    st.button("تحديث خطة الانتشار 🚀")