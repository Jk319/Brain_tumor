from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np
import cv2
import os
from PIL import Image

# ✅ Initialize Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# ✅ Load the trained model once at startup
model = joblib.load("model.pkl")  # Ensure model.pkl is in the root directory

# ✅ Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Check for image in form-data
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # ✅ Open and preprocess the image
        img = Image.open(file.stream).convert('L')   # Grayscale
        img = img.resize((100, 100))                 # Resize to match model input
        img_array = np.array(img).reshape(1, -1)     # Flatten to 1D

        # ✅ Predict with model
        prediction = model.predict(img_array)[0]
        result = "Tumor Detected" if prediction == 1 else "No Tumor"

        # ✅ Return JSON response
        return jsonify({'prediction': result})

    except Exception as e:
        print("❌ Prediction Error:", e)
        return jsonify({'error': str(e)}), 500

# ✅ Run the app (for local or Render.com)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use environment PORT or default 5000
    app.run(host='0.0.0.0', port=port, debug=True)



# from flask import Flask, request, render_template, jsonify
# import joblib
# import cv2
# import numpy as np
# import os
# from PIL import Image  # ✅ You missed this import

# app = Flask(__name__)
# model = joblib.load("model.pkl")  # Ensure model.pkl is in the correct directory

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         file = request.files['file'] 
#         img = Image.open(file.stream).convert('L')  # convert to grayscale
#         img = img.resize((100, 100))
#         img_array = np.array(img).reshape(1, -1)  # shape = (1, 10000)

#         pred = model.predict(img_array)[0]

#         result = 'Tumor Detected' if pred == 1 else 'No Tumor'
#         return jsonify({'prediction': result})

#     except Exception as e:
#         return jsonify({'error': str(e)})

# # ✅ Required for Render.com to work
# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port, debug=True)
