import streamlit as st
import joblib
import pandas as pd
from feature_extraction import extract_features

# Load the trained model
model = joblib.load("phishing_detector.pkl")

st.title("🔍 URL Phishing Detector")

url = st.text_input("Enter the URL to check:")

if st.button("Analyze"):
    try:
        features = extract_features(url)
        df = pd.DataFrame([features])  # Create DataFrame from dict
        prediction = model.predict(df)[0]
        if prediction == 1:
            st.error("⚠️ This is a phishing website!")
        else:
            st.success("✅ This is a legitimate website.")
    except Exception as e:
        st.warning(f"⚠️ Unable to classify this URL. Error: {e}")
