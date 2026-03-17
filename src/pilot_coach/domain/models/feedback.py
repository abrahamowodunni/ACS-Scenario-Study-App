from pydantic import BaseModel


class Feedback(BaseModel):
    accuracy_score: float
    risk_score: float
    completeness_score: float
    strengths: list[str]
    gaps: list[str]
    next_step: str
