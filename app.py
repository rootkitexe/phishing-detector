import streamlit as st
import pandas as pd
import joblib
from feature_extractor import extract_features  # your new function

# Load the trained model
model = joblib.load('phishing_detector.pkl')

st.set_page_config(page_title="Phishing Detector", page_icon="🛡️")
st.title("🛡️ Phishing Website Detection Tool")
st.markdown("Enter a website URL and check if it's **phishing** or **legitimate**.")

# UI Input
url = st.text_input("🔗 Enter URL")

if st.button("Check URL"):
    if url:
        try:
            features = extract_features(url)

            # If needed, remap to match model's expected features
            # Adjust keys based on your model's training features
            mapped_features = {
                'length_url': features['url_length'],
                'ip': features['uses_ip'],
                'nb_at': features['has_at_symbol'],
                'nb_hyphens': features['has_hyphen'],
                'https_token': features['uses_https'],
                'domain_age': features['domain_age']
            }

            features_df = pd.DataFrame([mapped_features])

            result = model.predict(features_df)[0]
            if result == 1:
                st.error("🚨 This is likely a **Phishing** site.")
            else:
                st.success("✅ This appears to be a **Legitimate** site.")
        except Exception as e:
            st.warning(f"⚠️ Unable to classify this URL.\nError: {e}")
    else:
        st.warning("Please enter a URL.")
