from flask import Flask, render_template, request, jsonify
from predict import predict_image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ✅ Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # ✅ Check if file is in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    # ✅ Check if file is selected (mobile-safe)
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    # ✅ Save file securely
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # ✅ Predict using your model
    result = predict_image(filepath)
    return jsonify({'prediction': result})

# ✅ Final setup for Render and local dev
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
