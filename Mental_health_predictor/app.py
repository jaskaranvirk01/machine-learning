import streamlit as st
import requests

API_URL = "https://mental-health-predictor-backend.onrender.com"

st.set_page_config(
    page_title="Mental Health Predictor",
    page_icon="🧠",
    layout="centered"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.block-container{
    max-width:800px;
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#1f4e79;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.result{
    padding:20px;
    border-radius:12px;
    text-align:center;
    background:#1E88E5;
    color:white;
    font-size:28px;
    font-weight:bold;
    margin-top:25px;
}

.stButton>button{
    width:100%;
    height:50px;
    font-size:18px;
    border-radius:8px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🧠 Student Mental Health Predictor</p>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Fill the details below to predict the Mental Health Score.</p>',
    unsafe_allow_html=True
)

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 10, 100, 20)

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        country = st.text_input(
            "Country",
            "India"
        )

        academic_level = st.selectbox(
            "Academic Level",
            ["Undergraduate",
             "Graduate",
             "High School"]
        )

        platform = st.selectbox(
            "Most Used Platform",
            [
                "Facebook",
                "Instagram",
                "LinkedIn",
                "Snapchat",
                "Twitter",
                "YouTube",
                "TikTok",
                "LINE",
                "KakaoTalk",
                "VKontakte",
                "WhatsApp",
                "WeChat"
            ]
        )

        purpose = st.selectbox(
            "Purpose of Use",
            [
                "Education",
                "Entertainment",
                "Networking",
                "News"
            ]
        )

    with col2:

        usage = st.slider(
            "Daily Usage Hours",
            0.0,
            24.0,
            5.0
        )

        unlocks = st.slider(
            "Daily Unlocks",
            0,
            300,
            50
        )

        study = st.slider(
            "Study Hours",
            0.0,
            12.0,
            4.0
        )

        physical = st.slider(
            "Physical Activity",
            0.0,
            10.0,
            1.0
        )

        sleep = st.slider(
            "Sleep Hours",
            0.0,
            12.0,
            7.0
        )

        stress = st.selectbox(
            "Stress Level",
            [
                "Low",
                "Medium",
                "High",
                "Very High"
            ]
        )

    submitted = st.form_submit_button("Predict Score")

if submitted:

    payload = {
        "age": age,
        "gender": gender,
        "country": country,
        "academic_level": academic_level,
        "most_used_platform": platform,
        "purpose_of_use": purpose,
        "avg_daily_usage_hours": usage,
        "daily_unlocks": unlocks,
        "study_hours": study,
        "physical_activity_hours": physical,
        "sleep_hours_per_night": sleep,
        "stress_level": stress,
    }

    with st.spinner("Predicting..."):

        try:

            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:

                score = response.json()["predicted_mental_health_score"]

                st.markdown(
                    f"""
                    <div class="result">
                        Predicted Mental Health Score
                        <br><br>
                        {score}/10
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.error("Prediction Failed")

        except Exception:
            st.error("Unable to connect to FastAPI server.")
