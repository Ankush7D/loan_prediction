import joblib

scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/svc_model.pkl")