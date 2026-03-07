from pydantic import BaseModel

class LoanInput(BaseModel):
    income: float
    age: float
    loan_amount: float
    credit_score: float
    dependents: float