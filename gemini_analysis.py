# gemini_analysis.py

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

        prompt = """Analyze the person in this image and craft a detailed, engaging personality profile. Your response should include:
                    - A precise estimation of age and gender
                    - Personality traits inferred from facial expressions, posture, grooming, and clothing style	
                    - The individual's emotional state at the moment the photo was taken
                    - Probable profession or lifestyle insights based on visual cues
                    - Cultural or stylistic elements (e.g., fashion choices, accessories, grooming habits)
                    - A comparison to a well-known Bollywood celebrity — who do they resemble most and why?
                    - Suggest the ideal work profile or career that aligns with their personality and visual demeanor
                    - End with a fun fact or quirky insight based solely on their appearance — keep it playful but respectful

                Ensure the tone is thoughtful, vivid, and conversational — like a blend of an expert profiler and a lifestyle coach with a touch of charm."""

        response = model.generate_content([prompt, img], stream=True)
        response.resolve()

        return response.text
    
    except Exception as e:
        return f"❌ Error during analysis: {e}"
