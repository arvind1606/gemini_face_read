import streamlit as st
from PIL import Image
from gemini_analysis import analyze_person_image

# --- Page Configuration ---
st.set_page_config(page_title="AI Profiler", page_icon="📷", layout="wide")

# --- Sidebar Info ---
with st.sidebar:
    st.markdown("## ℹ️ About This App")
    st.markdown("""
    This AI-powered image profiler uses **Google Gemini** to analyze uploaded images and generate a **personality profile** based on visual traits.

    **Steps to Use:**
    1. Upload your image
    2. Click **Analyze** to generate the profile

    ---
    ### 📬 About Author
    - **LinkedIn:** [Arvind Singh](https://www.linkedin.com/in/arvind-singh-1606)
    - **Email:** [arv.arvind1606@gmail.com](mailto:arv.arvind1606@gmail.com)
    """)

# --- App Header ---
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #3b3b3b;'>📷 AI-Powered Image Profiler</h1>
        <p style='color: gray; font-size: 18px;'>Upload an image to get an AI-generated personality profile using Google Gemini</p>
    </div>
    <hr style="margin-top: 10px; margin-bottom: 30px;">
""", unsafe_allow_html=True)

# --- Step 1: Upload Image ---
st.markdown("## 🎯 Step 1: Upload Your Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="✅ Uploaded Image", use_container_width=True)

    st.markdown("## 🧠 Step 2: Run the AI Analysis")

    if st.button("🔍 Analyze Image", use_container_width=True):
        with st.spinner("Analyzing image using Gemini AI..."):
            analysis = analyze_person_image(uploaded_file)
            st.success("✅ Analysis Complete!")

            st.markdown("### 🤖 Gemini Personality Profile")
            st.markdown(
                f"<div style='background-color:#f4f4f4;padding:20px;border-radius:10px;border:1px solid #e0e0e0;'>{analysis}</div>",
                unsafe_allow_html=True
            )
else:
    st.info("👆 Please upload an image file to proceed.")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 14px;'>Built with ❤️ using Streamlit and Gemini AI</div>",
    unsafe_allow_html=True
)
