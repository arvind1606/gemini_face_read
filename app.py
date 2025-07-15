# app.py

import streamlit as st
from PIL import Image
from webcam_utils import capture_webcam_image
from gemini_analysis import analyze_person_image

# Page config
st.set_page_config(page_title="Webcam AI Profiler", page_icon="📷", layout="centered")

# App header
st.markdown("<h1 style='text-align: center;'>📷 AI-Powered Webcam Profiler</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Capture an image and get an AI-generated personality profile using Gemini</p>", unsafe_allow_html=True)
st.markdown("---")

# Capture & Analyze Section
st.subheader("🎯 Step 1: Capture Your Image")

if st.button("📸 Capture Image", use_container_width=True):
    st.info("📡 Accessing webcam...")
    success, result = capture_webcam_image()

    if success:
        image = Image.open(result)
        st.image(image, caption="✅ Captured Image", use_container_width=True)

        st.markdown("---")
        st.subheader("🧠 Step 2: Gemini AI Analysis")

        with st.spinner("🔍 Analyzing image using Gemini AI..."):
            analysis = analyze_person_image(result)
            st.success("✅ Analysis Complete!")
            st.markdown("### 🤖 Gemini Personality Profile")
            st.markdown(f"<div style='background-color:#f9f9f9;padding:15px;border-radius:10px'>{analysis}</div>", unsafe_allow_html=True)
    else:
        st.error(f"❌ {result}")

# Footer
st.markdown("---")
st.markdown(
    "<small style='color: gray;'>Built with ❤️ using Streamlit and Google Gemini API</small>",
    unsafe_allow_html=True
)
