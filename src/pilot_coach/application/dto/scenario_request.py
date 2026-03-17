from pydantic import BaseModel, Field

from pilot_coach.domain.enums.certificate_type import CertificateType
from pilot_coach.domain.enums.study_mode import StudyMode


class ScenarioRequest(BaseModel):
    user_id: str = Field(default="demo-user")
    certificate_type: CertificateType = CertificateType.PRIVATE_PILOT_AIRPLANE
    task_code: str = Field(default="PA.I.A.K1")
    task_title: str = Field(default="Pilot Qualifications")
    difficulty: str = Field(default="medium")
    mode: StudyMode = StudyMode.SCENARIO
