from pydantic import BaseModel

from pilot_coach.domain.models.citation import Citation


class EvaluationResponse(BaseModel):
    accuracy_score: float
    risk_score: float
    completeness_score: float
    strengths: list[str]
    gaps: list[str]
    next_step: str
    citations: list[Citation]
