import streamlit as st
import numpy as np
import pickle
from PIL import Image
from utils import preprocess_image
import os

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "brain_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)
# UI
st.title("🧠 Brain Tumor Detection from MRI")
st.markdown("Upload an MRI scan and detect if a tumor is present.")

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI', use_column_width=True)

    img_array = preprocess_image(image)
    prediction = model.predict(img_array)

    label = "Tumor Detected 🚨" if prediction[0] == 1 else "No Tumor ✅"
    st.success(f"Prediction: **{label}**")
