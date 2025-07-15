# 📷 AI-Powered Webcam Profiler

This is a Streamlit-based web application that captures an image from your webcam and uses **Gemini AI** to generate a personality profile based on your appearance.

---

## 🚀 Features

- 📸 Capture a real-time image from your webcam  
- 🤖 Analyze the image using Google Gemini AI  
- 🧠 Predict interesting details like:  
  - Estimated age  
  - Emotional state  
  - Personality traits  
  - Possible lifestyle or profession  
- ⚡ Interactive and responsive UI with Streamlit

---

## 🧩 Tech Stack

- [Streamlit](https://streamlit.io/) – UI and app framework  
- [Pillow (PIL)](https://python-pillow.org/) – Image processing  
- Google Gemini API – For advanced image-to-text personality inference  
- `OpenCV` (via `webcam_utils.py`) – Webcam capture utility

---

## 🛠️ Project Structure

📁 your-project/
│
├── app.py # Main Streamlit app
├── webcam_utils.py # Webcam capture helper
├── gemini_analysis.py # Gemini image analysis logic
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 📌 What You’ll See
After running the app:
- You can capture an image using your webcam.
- The app displays the image and analyzes it with Gemini AI.
- You'll receive a rich personality profile including psychological and lifestyle insights.
