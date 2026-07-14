# ❤️ Heart Disease Prediction System

## 📌 Project Overview

The **Heart Disease Prediction System** is a Machine Learning web application that predicts whether a patient is likely to have heart disease based on medical attributes. The application is built using **Python**, **Scikit-learn**, and **Streamlit**, providing an interactive interface for users to enter patient information and receive instant predictions.

The model has been trained on a heart disease dataset using the **Random Forest Classifier**, and the trained model is deployed with Streamlit for real-time predictions.

---

# 🚀 Features

* Predicts the likelihood of heart disease.
* Interactive and user-friendly Streamlit interface.
* Uses a trained Random Forest Machine Learning model.
* Supports real-time prediction.
* Displays prediction confidence.
* Clean and responsive UI.
* Easy to deploy locally or on Streamlit Cloud.

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

# 🤖 Machine Learning Model

**Algorithm Used**

* Random Forest Classifier

**Preprocessing**

* Data Cleaning
* Feature Selection
* Standard Scaling (if applicable)
* Train-Test Split

**Model Evaluation**

* Accuracy Score
* Confusion Matrix
* Classification Report
* Cross Validation

---

# 📂 Dataset

The dataset contains medical information about patients used to predict heart disease.

### Features

* Age
* Sex
* Chest Pain Type
* Blood Pressure (BP)
* Cholesterol
* Fasting Blood Sugar over 120
* EKG Results
* Maximum Heart Rate
* Exercise-Induced Angina
* ST Depression
* Slope of ST Segment
* Number of Major Vessels
* Thallium Test

### Target

* Heart Disease

---

# 📁 Project Structure

```
Heart-Disease-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── heart_disease_model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── notebook/
│   └── Heart_Disease_Prediction.ipynb
│
├── dataset/
│   └── heart.csv
│
└── assets/
    └── images/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
```

Go to the project directory

```bash
cd Heart-Disease-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

---

# 📸 Application Workflow

1. Enter patient information.
2. Click the **Predict** button.
3. The model analyzes the input.
4. The application displays whether heart disease is predicted along with the prediction confidence.

---
# 📸 Screenshots

## 🏠 Home Page

<img width="1817" height="777" alt="Screenshot 2026-07-14 115340" src="https://github.com/user-attachments/assets/f5670cce-91cd-4eb2-be4f-a0f59b0fe922" />


---

## ❤️ Prediction Result

<img width="1822" height="525" alt="Screenshot 2026-07-14 115356" src="https://github.com/user-attachments/assets/90445538-b42e-467f-a0bf-b12efbad7d72" />



# 📊 Machine Learning Workflow

* Data Collection
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Train-Test Split
* Model Training
* Model Evaluation
* Model Saving using Joblib
* Streamlit Deployment

---

# 📦 Required Libraries

* streamlit
* pandas
* numpy
* scikit-learn
* joblib

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🔮 Future Improvements

* Add multiple machine learning algorithms for comparison.
* Improve prediction accuracy using hyperparameter tuning.
* Deploy the application on Streamlit Cloud.
* Add interactive visualizations and charts.
* Support batch prediction using CSV file upload.
* Include feature importance visualization.

---

# 👨‍💻 Author

**Zaheer Ahmed**

Computer Science Undergraduate
University of Turbat

### Connect with Me

* GitHub: https://github.com/zaheerbalochtech-gif
* LinkedIn: www.linkedin.com/in/zaheer-ahmed-54300338b

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support helps motivate future open-source projects and improvements.
