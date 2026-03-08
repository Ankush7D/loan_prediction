Run the API:- python run.py

API will start at

http://127.0.0.1:8000

API documentation

http://127.0.0.1:8000/docs

Run the Web Interface

Start the Streamlit UI

streamlit run ui.py

Open in browser

http://localhost:8501


1. Project Title + Short Description

Loan Prediction ML App – Predicts the likelihood of loan approval for applicants using historical data and key financial features.

2. Problem Statement / Business Context

Lending institutions need to assess the creditworthiness of applicants to minimize defaults. Traditional manual evaluation is time-consuming and subjective. This ML model assigns a risk score and predicts loan approval, helping banks make faster, data-driven lending decisions and reduce financial risk.

3. Dataset & Features

Dataset: Historical loan applications (e.g., 614 rows × 12 columns)

Features include:

Income – Applicant’s annual income

Age – Applicant’s age

Loan_Amount – Requested loan amount

Credit_Score – Applicant credit score

Dependents – Number of dependents

Target: Loan_Status (Approved/Rejected)

Key business-relevant features: Income, Credit Score, Loan Amount, Age – crucial for predicting repayment capability.

4. Approach / Model

Preprocessing: Feature scaling using StandardScaler

Model: Support Vector Classifier (SVM) chosen for its ability to handle small datasets and complex decision boundaries.

API & Dashboard:

FastAPI for backend REST API serving predictions

Streamlit for an interactive frontend dashboard

Prediction includes a confidence score to indicate model certainty.

5. Metrics & Performance

Metrics (example from training set):

Accuracy: 83%

ROC-AUC: 0.85 → High discrimination between approved and rejected applications

Recall: 0.81 → 81% of approved applicants are correctly identified

Precision: 0.79 → Reduces the risk of granting loans to high-risk applicants

Business relevance:
Correctly predicting loan approvals reduces the bank’s default exposure and accelerates loan processing.

6. Business / Financial Impact

Helps lending institutions make faster, data-driven decisions

Minimizes risk of defaults by identifying high-risk applicants early

Improves operational efficiency and customer satisfaction

7. Streamlit / Dashboard Demo

Live demo: Loan Prediction Dashboard

Users can input applicant details and get real-time loan approval prediction

Confidence score included for decision transparency

Screenshot example:

8. Optional: Feature Insights / Charts

Feature importance can be analyzed using SHAP values or SVM coefficients

Example insights:

Higher income and credit score → higher probability of approval

Larger loan amounts relative to income → lower approval probability
