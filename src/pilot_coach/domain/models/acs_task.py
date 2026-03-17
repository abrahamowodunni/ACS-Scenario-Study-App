from pydantic import BaseModel

from pilot_coach.domain.enums.certificate_type import CertificateType


class ACSTask(BaseModel):
    code: str
    title: str
    area_of_operation: str
    certificate_type: CertificateType
