import streamlit as st
import pandas as pd
import joblib

# ==========================================================
# Page Configuration
# ==========================================================
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ==========================================================
# Load Model
# ==========================================================
@st.cache_resource
def load_files():
    model = joblib.load("models/heart_disease_model.pkl")
    scaler = joblib.load("models/scaler.pkl")          # Remove if not used
    columns = joblib.load("models/heart_disease_columns.pkl")

    return model, scaler, columns


model, scaler, columns = load_files()

# ==========================================================
# Title
# ==========================================================
st.title("❤️ Heart Disease Prediction System")

st.markdown("""
Predict whether a patient is likely to have heart disease based on medical information.
""")

st.divider()

# ==========================================================
# User Inputs
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=40
    )

    sex = st.selectbox(
        "Sex",
        [0, 1],
        format_func=lambda x: "Female" if x == 0 else "Male"
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        [1, 2, 3, 4]
    )

    bp = st.number_input(
        "Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=50,
        max_value=700,
        value=200
    )

    fbs = st.selectbox(
        "FBS over 120 mg/dl",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    ekg = st.selectbox(
        "EKG Results",
        [0, 1, 2]
    )

with col2:

    max_hr = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150
    )

    exercise_angina = st.selectbox(
        "Exercise Angina",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    st_depression = st.number_input(
        "ST Depression",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    slope = st.selectbox(
        "Slope of ST",
        [1, 2, 3]
    )

    vessels = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3]
    )

    thallium = st.selectbox(
        "Thallium",
        [3, 6, 7]
    )

# ==========================================================
# Prediction
# ==========================================================

st.divider()

if st.button("Predict Heart Disease", use_container_width=True):

    input_df = pd.DataFrame([{
        "Age": age,
        "Sex": sex,
        "Chest pain type": chest_pain,
        "BP": bp,
        "Cholesterol": cholesterol,
        "FBS over 120": fbs,
        "EKG results": ekg,
        "Max HR": max_hr,
        "Exercise angina": exercise_angina,
        "ST depression": st_depression,
        "Slope of ST": slope,
        "Number of vessels fluro": vessels,
        "Thallium": thallium
    }])

    # Ensure correct column order
    input_df = input_df[columns]

    # Scale the data
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    # Probability
    probability = model.predict_proba(input_scaled)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")

    st.subheader("Prediction Confidence")

    st.progress(float(max(probability)))

    st.write(f"**No Heart Disease:** {probability[0]*100:.2f}%")
    st.write(f"**Heart Disease:** {probability[1]*100:.2f}%")