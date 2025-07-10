from flask import Flask, request, render_template, jsonify
import joblib
import cv2
import numpy as np
import os

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({'prediction': 'No file uploaded'})

        # Read and preprocess image
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (64, 64))
        img = img.flatten().reshape(1, -1)

        prediction = model.predict(img)[0]
        result = "Tumor Detected" if prediction == 1 else "No Tumor"
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# Required for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
