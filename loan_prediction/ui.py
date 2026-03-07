import streamlit as st
import numpy as np
import joblib

# Load scaler and model
scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/svc_model.pkl")

st.title("Loan Approval Predictor")
st.write("Enter applicant details to predict loan approval.")

income = st.number_input("Income", value=50000.0)
age = st.number_input("Age", value=30.0)
loan_amount = st.number_input("Loan Amount", value=200000.0)
credit_score = st.number_input("Credit Score", value=700.0)
dependents = st.number_input("Dependents", value=1.0)

if st.button("Predict"):

    # Prepare input
    x = np.array([[income, age, loan_amount, credit_score, dependents]])
    x_scaled = scaler.transform(x)
    
    # Prediction
    pred = model.predict(x_scaled)[0]
    prob = model.predict_proba(x_scaled).max() if hasattr(model, "predict_proba") else None
    label = "Approved" if pred == 1 else "Rejected"
    
    st.success(f"Loan Status: {label}")
    if prob:
        st.write(f"Confidence: {prob:.2f}")