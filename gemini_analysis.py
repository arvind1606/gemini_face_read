# gemini_analysis.py

import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Load environment variables (optional if you're using .env)
load_dotenv()

# Configure Gemini API Key
GEMINI_API_KEY = st.secrets["api_key"]
genai.configure(api_key=GEMINI_API_KEY)

def analyze_person_image(image_path='captured_image.jpg'):
    """
    Analyze a person's image using Gemini and return a descriptive profile.
    """
    try:
        img = Image.open(image_path)
        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = """Analyse the person in this image and provide a detailed profile including:
        - Estimated age and gender, try to be more precise
        - Personality traits based on facial expressions, posture, and style
        - Emotional state at the time of the photo
        - Possible profession or lifestyle hints
        - Cultural or stylistic cues (e.g., fashion, accessories, grooming)
        - Compare their appearance to public figures or fictional characters.
        Keep the tone engaging and insightful, also suggest what work profile is best suited for this person, also try to write a fun fact about the person based on the image."""

        response = model.generate_content([prompt, img], stream=True)
        response.resolve()

        return response.text
    
    except Exception as e:
        return f"❌ Error during analysis: {e}"
