import joblib
import cv2
import numpy as np

# Load the saved model
model = joblib.load('model.pkl')

def predict_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (100, 100)).flatten().reshape(1, -1)
    prediction = model.predict(img)
    return "Tumor Detected" if prediction[0] == 1 else "No Tumor"
