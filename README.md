# 🧠 Brain Tumor Detection from MRI Scans Images

This project detects brain tumors using MRI images via machine learning. A binary classifier predicts whether a brain scan is tumor-positive or not. It is deployed as a web-based diagnostic tool.

---

## 📁 Live Demo

**✨ Live Web App:** [https://brain-tumor-detect.onrender.com](https://brain-tumor-ggr5.onrender.com)

---

## 📀 Overview

* **Goal:** Classify MRI brain scans as *Tumor* or *No Tumor*.
* **Dataset:** 3,000 MRI images (1,500 tumor, 1,500 non-tumor) from Kaggle.
* **Pipeline:** Preprocessing → Feature Extraction → Model Training → Web Deployment.

---

## 🔮 Dataset

* **Source:** [Kaggle - Brain Tumor MRI Dataset](https://www.kaggle.com/datasets)
* **Classes:**

  * Tumor (Glioma, Meningioma, Pituitary)
  * Non-Tumor (Healthy Brain)
* **Total Images:** 3,000

---

## 🔧 Technologies Used

* **Language:** Python
* **ML Libraries:** Scikit-learn, NumPy, OpenCV
* **Web Technologies:** Flask, HTML5, CSS, JavaScript
* **Deployment:** Render.com

---

## ✨ Models Evaluated

| Model               | Accuracy | F1-Score |
| ------------------- | -------- | -------- |
| Logistic Regression | 96%      | 0.96     |
| Random Forest       | 96%      | 0.96     |
| Neural Network      | 95%      | 0.95     |
| SVC (Final Model)   | 94%      | 0.94     |
| KNN                 | 90%      | 0.91     |
| Naive Bayes         | 64%      | 0.63     |
| K-Means             | 64%      | 0.63     |

---

## 🛠️ Preprocessing

* **Noise Reduction:** Gaussian Blur
* **Normalization:** Scaling pixel values
* **Resizing:** 128x128 pixels
* **Augmentation:** Rotation, flipping, zoom

---

## 📊 Feature Extraction

* **Texture:** GLCM (Gray-Level Co-occurrence Matrix)
* **Histogram:** Intensity-based features
* **Flattening:** For traditional ML models

---

## 🔢 Evaluation Metrics

* Accuracy
* Precision & Recall
* F1-Score
* Confusion Matrix
* ROC Curve & AUC

---

## 🎉 Deployment (Web App)

* **Backend:** Flask handles file upload, preprocessing, and model prediction.
* **Frontend:** HTML/CSS/JS with image preview and mobile-friendly file input (gallery/camera).
* **Model:** Pickled `.pkl` file loaded during runtime.
* **Host:** Render.com free tier with GitHub integration.

---

## 🎯 Conclusion

The SVC model provided robust results (94% accuracy). The project shows how classical ML can be applied to medical imaging. Future improvements include CNN-based models and 3D segmentation.

---

## 🚀 Future Scope

* CNN or Transfer Learning models
* Grad-CAM visualization for tumor areas
* Mobile app version (React Native)
* 3D MRI support and segmentation

---

## 📂 Folder Structure

```
BrainTumorDetection/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── index.html
├── model.pkl
├── app.py
├── README.md
└── requirements.txt
```

---

## 👨‍💼 Author

**Jatin Kushwaha**
[GitHub](https://github.com/Jk319) • [LinkedIn](https://linkedin.com/in/jatin-kushwaha)

---

## 📄 License

This project is for educational and research purposes only. Not intended for real medical use.
