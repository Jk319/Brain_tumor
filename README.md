# 🧠 Brain Tumor Detection from MRI Scans

This project focuses on detecting brain tumors using MRI images through machine learning techniques. A binary classification system was developed and evaluated across multiple models to assist in early, non-invasive diagnosis.

---

## 📌 Overview

- **Goal:** Classify MRI brain scans as *tumor* or *non-tumor*.
- **Dataset:** 3,000 MRI images from Kaggle (1,500 tumor, 1,500 non-tumor).
- **Approach:** Image preprocessing → Feature extraction → Model training → Evaluation.

---

## 🧪 Dataset

- **Source:** [Kaggle - Brain Tumor MRI Dataset](https://www.kaggle.com/datasets)
- **Classes:**
  - Tumor: Glioma, Meningioma, Pituitary
  - Non-Tumor: Healthy Brain
- **Total Images:** 3,000 (Split evenly for training and testing)

---

## 🔧 Technologies Used

- **Language:** Python  
- **Libraries:** Scikit-learn, OpenCV, NumPy, Matplotlib  
- **Models Tested:**  
  - Logistic Regression  
  - Support Vector Classifier (SVC)  
  - K-Nearest Neighbors (KNN)  
  - Neural Networks  
  - Random Forest  
  - Naive Bayes  
  - K-Means (unsupervised)

---

## 🧼 Preprocessing Steps

- Noise reduction using Gaussian filtering  
- Normalization for consistent brightness/contrast  
- Augmentation: rotation, flipping, scaling

---

## 🎯 Feature Extraction

- **Texture:** GLCM (Gray Level Co-occurrence Matrix)  
- **Shape & Intensity:** Histogram analysis of pixel values

---

## 🧠 Model Performance

| Model              | Accuracy | F1-Score |
|-------------------|----------|----------|
| Logistic Regression | 96%      | 0.96     |
| Random Forest       | 96%      | 0.96     |
| Neural Network      | 95%      | 0.95     |
| SVC                 | 94%      | 0.94     |
| KNN                 | 90%      | 0.91     |
| Naive Bayes         | 64%      | 0.63     |
| K-Means Clustering  | 64%      | 0.63     |

---

## 📊 Evaluation Metrics

- Accuracy  
- Precision & Recall  
- F1-Score  
- Confusion Matrix  
- ROC Curve & AUC

---

## 📌 Conclusion

Logistic Regression and Random Forest achieved the best performance with 96% accuracy. The project demonstrates how machine learning can be applied to medical imaging for early tumor detection.

---

## 🚀 Future Work

- Deploy as a web-based diagnostic tool  
- Integrate deep learning (CNNs) for further accuracy  
- Use 3D MRI datasets for advanced segmentation

---

## 📁 Folder Structure
📦BrainTumorDetection
┣ 📁 images/ # Sample MRI scans
┣ 📁 models/ # Trained model files (if saved)
┣ 📜 brain_tumor_project.ipynb
┣ 📜 README.md
┗ 📜 requirements.txt


---

## 👨‍💻 Author

**Jatin Kushwaha**  
[GitHub](https://github.com/Jk319) | [LinkedIn](https://linkedin.com/in/jatin-kushwaha)

---

## 📄 License

This project is for educational and research purposes only.

