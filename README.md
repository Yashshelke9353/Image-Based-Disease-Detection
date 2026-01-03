# 🩺 Image-Based Disease Detection using Chest X-Ray Images

## 📌 Project Overview
This project uses Deep Learning (Convolutional Neural Networks - CNN) to classify chest X-ray images into three categories:
- **NORMAL**
- **PNEUMONIA**
- **COVID-19**

The goal of this project is to assist in early detection of respiratory diseases using medical imaging and artificial intelligence.

---

## 🎯 Objective
To build a multi-class image classification model that can accurately detect diseases from chest X-ray images.

---

## 📂 Dataset Information
- Dataset Type: Chest X-ray Images
- Classes:
  - NORMAL
  - PNEUMONIA
  - COVID
- Source: Kaggle (Chest X-ray datasets)
- Note: Due to the large size of the dataset, it is **not uploaded** to this GitHub repository.

---

## 📁 Folder Structure


chest_xray/
├── train/
│ ├── NORMAL/
│ ├── PNEUMONIA/
│ └── COVID/
├── val/
│ ├── NORMAL/
│ ├── PNEUMONIA/
│ └── COVID/
└── test/
├── NORMAL/
├── PNEUMONIA/
└── COVID/



---

## 🛠️ Technologies Used
- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🧠 Model Architecture
- Convolutional Neural Network (CNN)
- Multiple Conv2D and MaxPooling layers
- Dense layer with Softmax activation for multi-class classification

---

## 📊 Model Evaluation
The model performance is evaluated using:
- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score

These metrics help in understanding how well the model performs on unseen test data.

---

## 🚀 How to Run the Project
1. Clone this repository
2. Install required dependencies using:



3. Download the dataset separately and arrange it in the required folder structure
4. Run the training notebook/script
5. Test the model using new chest X-ray images

---

## 📌 Results
The trained CNN model successfully classifies chest X-ray images into Normal, Pneumonia, and COVID categories with good accuracy.

---

## ⚠️ Important Note
The dataset is not included in this repository due to its large size.  
Please download it separately before running the project.

---

## 👤 Author
**Yash Shelke**  
Intern at **Codectechnologies**

---

## ⭐ Acknowledgement
Thanks to Kaggle and the open-source community for providing the datasets and learning resources.
