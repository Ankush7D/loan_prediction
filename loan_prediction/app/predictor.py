import numpy as np
from .model_loader import scaler, model

def make_prediction(data):

    values = np.array([[
        data.income,
        data.age,
        data.loan_amount,
        data.credit_score,
        data.dependents
    ]])

    scaled = scaler.transform(values)

    prediction = model.predict(scaled)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(scaled).max())

    label = "Approved" if prediction == 1 else "Rejected"

    return label, probability