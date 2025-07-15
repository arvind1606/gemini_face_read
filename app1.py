# app.py

import streamlit as st
from PIL import Image
from gemini_analysis import analyze_person_image

# Page config
st.set_page_config(page_title="AI Profiler", page_icon="📷", layout="centered")

# App header
st.markdown("<h1 style='text-align: center;'>📷 AI-Powered Image Profiler</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Upload an image to get an AI-generated personality profile using Gemini</p>", unsafe_allow_html=True)
st.markdown("---")

# Step 1: Upload image
st.subheader("🎯 Step 1: Upload Your Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="✅ Uploaded Image", use_container_width=True)

    st.markdown("---")
    st.subheader("🧠 Step 2: Run Gemini AI Analysis")

    # Step 2: Analyze button
    if st.button("🔍 Analyze Image", use_container_width=True):
        with st.spinner("Analyzing image using Gemini AI..."):
            analysis = analyze_person_image(uploaded_file)
            st.success("✅ Analysis Complete!")
            st.markdown("### 🤖 Gemini Personality Profile")
            st.markdown(
                f"<div style='background-color:#f9f9f9;padding:15px;border-radius:10px'>{analysis}</div>",
                unsafe_allow_html=True
            )
else:
    st.info("👆 Please upload an image file to proceed.")

# Footer
st.markdown("---")
st.markdown(
    "<small style='color: gray;'>Built with ❤️ using Streamlit and Google Gemini API</small>",
    unsafe_allow_html=True
)
