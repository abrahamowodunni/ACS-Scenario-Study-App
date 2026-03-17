from pydantic import BaseModel


class ScenarioStructuredOutput(BaseModel):
    title: str
    scenario: str
    follow_up_question: str
