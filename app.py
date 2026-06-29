import streamlit as st
import pandas as pd
import joblib


model           = joblib.load('knn_heart_model.pkl')
scaler          = joblib.load('scaler.pkl')
expected_cols   = joblib.load('columns.pkl')


st.title("❤️ Heart Stroke Prediction Portal")
st.markdown("### Provide the following medical details:")

# ─── COLLECT USER INPUTS ──────────────────────────────────
age             = st.slider("Age", 18, 100, 40)
sex             = st.selectbox("Sex", ["Male", "Female"])
chest_pain      = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
resting_bp      = st.number_input("Resting Blood Pressure (mmHg)", 80, 200, 120)
cholesterol     = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs      = st.selectbox("Fasting Blood Sugar > 120 mg/dL?", [0, 1])
resting_ecg     = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr          = st.slider("Max Heart Rate Achieved", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina?", ["Yes", "No"])
oldpeak         = st.number_input("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope        = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# ─── PREDICT BUTTON ───────────────────────────────────────
if st.button("🔍 Predict"):

    # Build raw input dictionary (matching original CSV column names)
    raw_input = {
        'Age':            age,
        'RestingBP':      resting_bp,
        'Cholesterol':    cholesterol,
        'FastingBS':      fasting_bs,
        'MaxHR':          max_hr,
        'Oldpeak':        oldpeak,
        # Categorical columns (will be one-hot encoded below)
        'Sex':            sex,
        'ChestPainType':  chest_pain,
        'RestingECG':     resting_ecg,
        'ExerciseAngina': exercise_angina,
        'ST_Slope':       st_slope
    }

    # ─── ONE-HOT ENCODE USER INPUT ────────────────────────
    input_df = pd.DataFrame([raw_input])

    input_encoded = pd.get_dummies(input_df, columns=[
        'Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'
    ])

    # ─── ALIGN COLUMNS WITH TRAINING DATA ─────────────────
    # Add missing columns as 0, drop extra columns
    for col in expected_cols:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    input_encoded = input_encoded[expected_cols]  # Keep only expected columns

    # ─── SCALE INPUT ──────────────────────────────────────
    input_scaled = scaler.transform(input_encoded)

    # ─── MAKE PREDICTION ──────────────────────────────────
    prediction = model.predict(input_scaled)[0]

    # ─── SHOW RESULT ──────────────────────────────────────
    st.markdown("---")
    if prediction == 1:
        st.error("⚠️ HIGH RISK of Heart Disease detected!")
        st.markdown("Please consult a cardiologist immediately.")
    else:
        st.success("✅ LOW RISK of Heart Disease.")
        st.markdown("Keep maintaining a healthy lifestyle!")

    # Show input summary
    with st.expander("View Input Summary"):
        st.dataframe(input_encoded)