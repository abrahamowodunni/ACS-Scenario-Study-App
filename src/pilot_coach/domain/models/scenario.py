from pydantic import BaseModel

from pilot_coach.domain.models.citation import Citation


class Scenario(BaseModel):
    title: str
    prompt: str
    follow_up_question: str | None = None
    citations: list[Citation] = []
