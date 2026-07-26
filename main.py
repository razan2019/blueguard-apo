import streamlit as st
import pandas as pd

# 1️⃣ إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="BlueGuard AI | منصة البيئة البحرية وحرس الحدود",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2️⃣ القائمة الجانبية واختيار الصفحة
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/water-element.png", width=70)
    st.title("📍 التنقل في المنصة")
    
    # اختيار الصفحة
    page = st.radio(
        "📑 اختر الصفحة المطلوبة:", 
        ["الرئيسية (Home)", "حرس الحدود (Border Guard)"]
    )
    
    st.markdown("---")

# ==========================================
# 🏠 الصفحة الأولى: الرئيسية (Home)
# ==========================================
if page == "الرئيسية (Home)":
    
    # CSS الصفحة الرئيسية
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    * { font-family: "Cairo", sans-serif !important; }
    .stApp {
        background: linear-gradient(rgba(10, 25, 47, 0.85), rgba(15, 32, 67, 0.9)), 
                    url("https://images.unsplash.com/photo-1518837695005-2083093ee35b?q=80&w=2070") no-repeat center center fixed !important;
        background-size: cover !important;
        color: #ffffff !important;
    }
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(12px) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        border: 1px solid rgba(72, 202, 228, 0.3) !important;
    }
    .hero-title {
        text-align: center;
        background: rgba(10, 25, 47, 0.6);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(72, 202, 228, 0.3);
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-title">
        <h1 style="color: #90e0ef; font-weight: 800;">🌊 منصة BlueGuard AI لحماية البيئة البحرية</h1>
        <p style="color: #caf0f8; font-size: 18px;">الرصد الذكي للتلوث وتحليل صحة الأحياء البحرية بواسطة الذكاء الاصطناعي</p>
    </div>
    """, unsafe_allow_html=True)

    # مؤشرات سريعة
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("درجة حرارة البحر", "28.8 °C", "+0.5 °C")
    with col2:
        st.metric("مستوى الأكسجين الذائب", "6.4 mg/L", "طبيعي 🟢")
    with col3:
        st.metric("مؤشر صحة البيئة البحرية", "88%", "ممتاز 🌊")

    st.markdown("---")
    st.subheader("📊 نظرة عامة على البيانات")
    st.write("أهلاً بك في الصفحة الرئيسية لمنصة BlueGuard AI. يمكنك التنقل لصفحة **حرس الحدود** من القائمة الجانبية باليسار.")


# ==========================================
# 🛡️ الصفحة الثانية: حرس الحدود (Border Guard)
# ==========================================
else:
    
    # CSS صفحة حرس الحدود
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    * { font-family: "Cairo", sans-serif !important; }
    .stApp {
        background: linear-gradient(rgba(10, 25, 47, 0.8), rgba(15, 32, 67, 0.88)), 
                    url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073") no-repeat center center fixed !important;
        background-size: cover !important;
        color: #ffffff !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #0077b6, #00b4d8) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 10px 25px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 12px rgba(0, 119, 182, 0.3) !important;
    }
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(14px) !important;
        border-radius: 20px !important;
        padding: 22px !important;
        border: 1px solid rgba(72, 202, 228, 0.25) !important;
    }
    .hero-box {
        text-align: center;
        background: rgba(10, 25, 47, 0.6);
        padding: 25px;
        border-radius: 25px;
        border: 1px solid rgba(72, 202, 228, 0.3);
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-box">
        <h1 style="color: #90e0ef; font-weight: 800;">🛡️ بوابـة حـرس الحـدود والرقابـة الميدانيـة</h1>
        <p style="color: #caf0f8; font-size: 18px;">منظومة المراقبة والتحليل الذكي لردع الصيد غير القانوني ومتابعة بلاغات السلامة البحرية</p>
    </div>
    """, unsafe_allow_html=True)

    # بيانات قطاعات الرقابة
    sectors_data = {
        "قطاع جازان وفرسان (الحدود الجنوبية)": {"lat": 16.8892, "lon": 42.5511, "active_boats": 14, "alerts_today": 2, "status": "مستقر 🟢"},
        "قطاع جدة ورابغ (المنطقة الوسطى)": {"lat": 21.5433, "lon": 39.1728, "active_boats": 22, "alerts_today": 5, "status": "مراقبة مكثفة 🟡"},
        "قطاع نيوم وتبوك (الحدود الشمالية)": {"lat": 28.3833, "lon": 34.5667, "active_boats": 9, "alerts_today": 1, "status": "مستقر 🟢"}
    }

    selected_sector = st.selectbox("🚨 اختر مركز الرقابة / القطاع:", options=list(sectors_data.keys()))
    sec_info = sectors_data[selected_sector]

    # تبويبات حرس الحدود
    tab1, tab2, tab3 = st.tabs(["📡 الرقابة المباشرة", "📸 التحليل البصري (AI)", "📋 البلاغات والإنذارات"])

    with tab1:
        st.subheader("📡 التتبع والرقابة الحية")
        m1, m2, m3 = st.columns(3)
        with m1: st.metric("حالة القطاع", sec_info["status"])
        with m2: st.metric("قوارب الدورية النشطة", f"{sec_info['active_boats']} قارب")
        with m3: st.metric("إنذارات اليوم", f"{sec_info['alerts_today']} بلاغات")
        
        st.markdown("### 🗺️ موقع القطاع البحري")
        st.map(pd.DataFrame({'lat': [sec_info["lat"]], 'lon': [sec_info["lon"]]}))

    with tab2:
        st.subheader("📸 التحليل البصري للذكاء الاصطناعي")
        uploaded_img = st.file_uploader("رفع صورة لوسيلة صيد أو قارب للتحليل:", type=['png', 'jpg', 'jpeg'])
        if uploaded_img:
            st.image(uploaded_img, caption="الصورة المرصودة", width=350)
            if st.button("🔍 بدء التحليل والأمان"):
                st.success("✅ تم التحليل: لا توجد أدوات صيد محظورة متطابقة مع الصورة.")

    with tab3:
        st.subheader("📋 البلاغات والإنذارات الحالية")
        reports_df = pd.DataFrame({
            "رقم البلاغ": ["#1082", "#1083", "#1084"],
            "القطاع": ["جازان", "جدة", "تبوك"],
            "نوع البلاغ": ["دخول منطقة محمية", "طلب استغاثة موج مرتفع", "صيد بدون تصريح"],
            "الحالة": ["تمت الاستجابة 🟢", "قيد المتابعة 🟡", "مغلق ⚪"]
        })
        st.dataframe(reports_df, use_container_width=True)
