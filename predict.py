from joblib import load
import cv2
import numpy as np

model = load("model.pkl") # or whatever your model path is

def predict_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (100, 100))
    img = img.flatten().reshape(1, -1)
    prediction = model.predict(img)
    return "Tumor" if prediction[0] == 1 else "No Tumor"
