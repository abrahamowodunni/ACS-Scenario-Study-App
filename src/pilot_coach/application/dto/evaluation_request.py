from pydantic import BaseModel


class EvaluationRequest(BaseModel):
    user_id: str = "demo-user"
    task_code: str = "PA.I.A.K1"
    question: str
    answer: str
