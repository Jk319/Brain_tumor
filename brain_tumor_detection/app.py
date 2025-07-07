import os
import joblib
import streamlit as st
from PIL import Image
import numpy as np
from utils import preprocess_image

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "brain_model.joblib")
model = joblib.load(model_path)

# Streamlit App UI
st.set_page_config(page_title="Brain Tumor Detector")
st.title("🧠 Brain Tumor Detection from MRI")

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded MRI", use_column_width=True)

    img_array = preprocess_image(image)
    prediction = model.predict(img_array)
    
    result = "🚨 Tumor Detected" if prediction[0] == 1 else "✅ No Tumor"
    st.success(f"Prediction: **{result}**")
