# 🚢 Titanic Survival Prediction 

🌐 **Live Demo:** [Click Here to Try the App](https://titanic-survival-prediction-93am.onrender.com)

---

## 📊 Project Summary

This project predicts passenger survival on the Titanic using machine learning models. It includes data cleaning, feature engineering, exploratory data analysis (EDA), model training, and deployment.

---

## 🔎 Initial Data Assessment

- Loaded `tested.csv` dataset.
- Target variable: **Survived** (1 = Survived, 0 = Did not survive).
- Found missing values in **Age**.
- Created features:
  - Total Family Members = `SibSp + Parch + 1`
  - Individual Fare = `Fare / Total Family Members`
- Handled categorical columns: **Gender**, **Embarked**.

---

## 🛠️ Data Preprocessing & Feature Engineering

- Handled missing values in **Age**, **Fare**, and **Embarked**.
- Dropped less relevant columns: `Cabin`, `Name`, `Ticket`.
- Encoded categorical columns (**Gender**, **Embarked**).
- Created:
  - `Total Family Members`
  - `Individual Fare`

---

## 📈 Exploratory Data Analysis (EDA)

- 📊 **Findings:**
  - Males had lower survival rates than females.
  - Most third-class passengers didn’t survive.
  - Traveling alone reduced survival chances.
  
- 🖼️ Visuals included:
  - Age distribution histogram
  - Survival count by gender
  - Class vs survival rate plots

---

## 🤖 Model Training & Evaluation

Trained three classification models on processed data:

| Model                  | Accuracy | Confusion Matrix |
|------------------------|----------|------------------|
| Logistic Regression    | 1.00     | `[[53 0], [0 31]]` |
| Random Forest Classifier | 1.00   | `[[53 0], [0 31]]` |
| XGBoost Classifier     | 1.00     | `[[53 0], [0 31]]` |

⚠️ **Note:** 100% accuracy suggests possible overfitting or data leakage (requires further validation).

---

## 💾 Model Saving

- Trained models saved using `joblib`:
  - `LogReg_model.pkl`
  - `random_forest_model.pkl`
  - `xgb_model.pkl`

---

## 🚀 Deployment

- Built a **Flask** web app for live predictions.
- Users can input passenger details and select the model.
- App deployed using **Render** platform.

---

## ✅ Tech Stack

- **Python, Flask, joblib**
- **scikit-learn, XGBoost**
- **Render (for deployment)**

---

## 📦 Installation (Optional for Local Run)

```bash
git clone https://github.com/tejoess/titanic-predictor.git
cd flask-app
pip install -r requirements.txt
python app.py
