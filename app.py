from flask import Flask, request, render_template, jsonify
import joblib
import cv2
import numpy as np
import os
from PIL import Image  # ✅ You missed this import

app = Flask(__name__)
model = joblib.load("model.pkl")  # Ensure model.pkl is in the correct directory

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file'] 
        img = Image.open(file.stream).convert('L')  # convert to grayscale
        img = img.resize((100, 100))
        img_array = np.array(img).reshape(1, -1)  # shape = (1, 10000)

        pred = model.predict(img_array)[0]

        result = 'Tumor Detected' if pred == 1 else 'No Tumor'
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# ✅ Required for Render.com to work
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
