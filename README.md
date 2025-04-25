
# Credit Risk Prediction using Machine Learning

This project uses the German Credit dataset to classify loan applicants into Good or Bad credit risk categories using machine learning models. It includes detailed data processing, model comparison, and an interactive Streamlit web app for real-time predictions.

## 🔍 Problem Statement
Financial institutions need efficient and accurate tools to assess credit risk. This project builds an ML pipeline to:
- Preprocess and analyze data
- Train and evaluate classifiers
- Predict credit risk in real-time using a Streamlit app

---

## 🧠 Models Used
- Logistic Regression (Baseline)
- Random Forest Classifier (Final Model)

---

## 📦 Project Structure

```
├── app.py                     # Streamlit App Code
├── rf_model.pkl              # Trained Random Forest Model
├── scaler.pkl                # StandardScaler object for numeric features
├── german_credit_data.csv    # Input Dataset

```

---

## ▶️ How to Run the App Locally

1. ✅ Clone the repo:

2. ✅ Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. ✅ Install required libraries:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install pandas numpy scikit-learn streamlit joblib matplotlib seaborn
```

4. ✅ Run the Streamlit App:

```bash
streamlit run app.py
```

This will launch the app in your browser at http://localhost:8501

---

## 📽 Demo Video

🎥 Watch the full walkthrough here:  
[📺 Demo ](https://drive.google.com/file/d/1W4xpx11AMx1OtEy6AP-aC7KvAs8ipW61/view?usp=sharing)

---

## 📁 Dataset Source

- UCI German Credit Dataset  
- Custom target variable created based on credit amount, duration, and financial health indicators.

---
