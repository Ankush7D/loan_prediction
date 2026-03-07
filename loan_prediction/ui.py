import streamlit as st
import requests

st.title("Loan Approval Predictor")

st.write("Enter applicant details to predict loan approval.")

income = st.number_input("Income", value=50000.0)
age = st.number_input("Age", value=30.0)
loan_amount = st.number_input("Loan Amount", value=200000.0)
credit_score = st.number_input("Credit Score", value=700.0)
dependents = st.number_input("Dependents", value=1.0)

if st.button("Predict"):

    url = "http://127.0.0.1:8000/predict"

    payload = {
        "income": income,
        "age": age,
        "loan_amount": loan_amount,
        "credit_score": credit_score,
        "dependents": dependents
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Loan Status: {result['loan_status']}")
        st.write(f"Confidence: {result['confidence']}")
    else:
        st.error("API error")