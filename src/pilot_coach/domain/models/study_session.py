from pydantic import BaseModel

from pilot_coach.domain.enums.study_mode import StudyMode


class StudySession(BaseModel):
    session_id: str
    user_id: str
    task_code: str
    mode: StudyMode
