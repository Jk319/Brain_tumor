# model.py
import joblib
from sklearn.svm import SVC
import numpy as np
import cv2
import os

def extract_features(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (100, 100)).flatten()
    return img

def train_model():
    # Example: You must replace this with your dataset
    X = []
    y = []

    for label in ['yes', 'no']:
        folder = f"data/{label}"
        for img_file in os.listdir(folder):
            path = os.path.join(folder, img_file)
            features = extract_features(path)
            X.append(features)
            y.append(1 if label == 'yes' else 0)

    model = SVC(probability=True)
    model.fit(X, y)
    joblib.dump(model, 'model.pkl')
    print("Model trained and saved as model.pkl")

if __name__ == "__main__":
    train_model()
