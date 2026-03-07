from fastapi import FastAPI, HTTPException
from .schema import LoanInput
from .predictor import make_prediction
from .logger import logger

app = FastAPI(
    title="Loan Prediction API",
    description="Machine Learning API for predicting loan approval",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict")
def predict(data: LoanInput):
    
    try:
        logger.info("Received prediction request")

        prediction, probability = make_prediction(data)

        logger.info(f"Prediction result: {prediction}")

        return {
            "loan_status": prediction,
            "confidence": probability
        }

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction error")