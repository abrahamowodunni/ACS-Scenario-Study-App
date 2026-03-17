from pydantic import BaseModel

from pilot_coach.domain.models.citation import Citation


class ScenarioResponse(BaseModel):
    title: str
    scenario: str
    follow_up_question: str
    citations: list[Citation]
