import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
from PIL import Image
import numpy as np

st.title("📷 Webcam Capture in Streamlit")

# Page config
st.set_page_config(page_title="Webcam AI Profiler", page_icon="📷", layout="centered")

# App header
st.markdown("<h1 style='text-align: center;'>📷 AI-Powered Webcam Profiler</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Capture an image and get an AI-generated personality profile using Gemini</p>", unsafe_allow_html=True)
st.markdown("---")

# Capture & Analyze Section
st.subheader("🎯 Step 1: Capture Your Image")

FRAME_CAPTURED = None

# Callback to process video frames
def video_frame_callback(frame):
    global FRAME_CAPTURED
    img = frame.to_ndarray(format="bgr24")
    FRAME_CAPTURED = img
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# Start webcam streamer
ctx = webrtc_streamer(
    key="example",
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
)

# Capture the current frame and analyze
if st.button("📸 Capture Frame"):
    if FRAME_CAPTURED is not None:
        img = Image.fromarray(cv2.cvtColor(FRAME_CAPTURED, cv2.COLOR_BGR2RGB))
        st.image(img, caption="Captured Frame", use_container_width=True)

        st.markdown("---")
        st.subheader("🧠 Step 2: Gemini AI Analysis")

        with st.spinner("🔍 Analyzing image using Gemini AI..."):
            analysis = analyze_person_image(result)
            st.success("✅ Analysis Complete!")
            st.markdown("### 🤖 Gemini Personality Profile")
            st.markdown(f"<div style='background-color:#f9f9f9;padding:15px;border-radius:10px'>{analysis}</div>", unsafe_allow_html=True)

    else:
        st.warning("No frame captured yet. Try again after video starts.")
