
import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')

# Encoding maps (these should match LabelEncoder logic)
sex_map = {'female': 0, 'male': 1}
housing_map = {'free': 0, 'own': 1, 'rent': 2}
saving_map = {'unknown': 0, 'little': 1, 'moderate': 2, 'quite rich': 3, 'rich': 4}
checking_map = {'unknown': 0, 'little': 1, 'moderate': 2, 'rich': 3}
purpose_map = {'radio/TV': 0, 'education': 1, 'furniture/equipment': 2, 'car': 3, 'business': 4, 'domestic appliances': 5, 'repairs': 6, 'vacation/others': 7}

# Streamlit UI
st.title("Credit Risk Predictor")
st.write("Enter the details below to assess credit risk")

age = st.slider("Age", 18, 75, 30)
sex = st.selectbox("Sex", list(sex_map.keys()))
job = st.selectbox("Job Type (0�3)", [0, 1, 2, 3])
housing = st.selectbox("Housing", list(housing_map.keys()))
saving = st.selectbox("Saving Accounts", list(saving_map.keys()))
checking = st.selectbox("Checking Account", list(checking_map.keys()))
credit_amount = st.number_input("Credit Amount", 100, 20000, 5000)
duration = st.slider("Duration (months)", 6, 72, 24)
purpose = st.selectbox("Purpose", list(purpose_map.keys()))

if st.button("Predict Credit Risk"):
    # Encode
    row = pd.DataFrame([{
        'Age': age,
        'Sex': sex_map[sex],
        'Job': job,
        'Housing': housing_map[housing],
        'Saving accounts': saving_map[saving],
        'Checking account': checking_map[checking],
        'Credit amount': credit_amount,
        'Duration': duration,
        'Purpose': purpose_map[purpose]
    }])

    # Scale numerical columns
    row[['Age', 'Credit amount', 'Duration']] = scaler.transform(row[['Age', 'Credit amount', 'Duration']])
    
    pred = model.predict(row)[0]
    st.success("Credit Risk: **{}**".format("Bad" if pred == 1 else "Good"))
