from flask import Flask, request, render_template, jsonify
import joblib
import cv2
import numpy as np
import os

app = Flask(__name__)
model = joblib.load("model.pkl")  # Make sure this file is in your GitHub repo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file uploaded'})

        # Convert image to format suitable for model
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (64, 64))
        img = img.flatten().reshape(1, -1)

        prediction = model.predict(img)[0]
        result = "Tumor Detected" if prediction == 1 else "No Tumor"
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

# ✅ FIX: Render requires this PORT setup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Don't use hardcoded port like 10000
    app.run(host='0.0.0.0', port=port, debug=True)
