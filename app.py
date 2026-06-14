import streamlit as st
import cv2
import numpy as np
import pickle
import requests
from urllib.parse import urlparse
from feature_extraction import extract_features

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="QR Security Checker", layout="centered")

st.title("🔐 QR Code Security Checker")
st.markdown("Upload a QR code to check if it is **Safe or Phishing**")

uploaded_file = st.file_uploader("Upload QR Code", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if not data:
        st.error("❌ No QR code detected")
    else:
        # Redirection
        try:
            response = requests.get(data, allow_redirects=True, timeout=5)
            final_url = response.url
        except:
            final_url = data

        parsed = urlparse(final_url)
        domain = parsed.netloc

        # Extract features & predict
        features = extract_features(final_url)
        result = model.predict([features])

        # 🔥 ===== SECURITY RESULT AT TOP =====
        st.markdown("## 🔍 Security Analysis")

        if result[0] == 1:
            st.markdown(
                f"""
                <div style="padding:15px; border-radius:10px; background-color:#ff4b4b; color:white; font-size:20px; text-align:center;">
                ⚠️ PHISHING WEBSITE DETECTED
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="padding:15px; border-radius:10px; background-color:#00c853; color:white; font-size:20px; text-align:center;">
                ✅ SAFE WEBSITE
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")

        # 🌐 Website Info
        st.subheader("🌐 Website Details")
        st.write(f"**Redirected Website:** {domain}")

        st.markdown("---")

        # 📷 Smaller QR image (below result)
        st.image(img, caption="Uploaded QR Code", width=200)