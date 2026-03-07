Loan Prediction System (FastAPI + ML)

A production-style Machine Learning API that predicts loan approval using a trained Scikit-learn model.
The system exposes a REST API built with FastAPI and includes a Streamlit dashboard for interactive predictions.

This project demonstrates ML model deployment, API development, and frontend integration.


Project Architecture
User Interface (Streamlit)
        │
        ▼
FastAPI REST API
        │
        ▼
Data Validation (Pydantic)
        │
        ▼
Feature Scaling (StandardScaler)
        │
        ▼
SVM Machine Learning Model
        │
        ▼
Prediction + Confidence Score.


Tech Stack

- Python

- FastAPI

- Scikit-learn

- NumPy

- Streamlit

- Uvicorn

- Joblib


Run the API:-
python run.py

API will start at

http://127.0.0.1:8000

API documentation

http://127.0.0.1:8000/docs


Run the Web Interface

Start the Streamlit UI

streamlit run ui.py

Open in browser

http://localhost:8501



Future Improvements:-

Model monitoring and logging

Docker containerization

Cloud deployment

Authentication for API endpoints



Author:-

Ankush Dutta
Computer Science Student | Machine Learning & Backend Development