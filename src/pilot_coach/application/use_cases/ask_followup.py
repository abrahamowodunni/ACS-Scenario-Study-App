from dataclasses import dataclass

from pilot_coach.application.services.oral_exam_service import OralExamService
from pilot_coach.shared.template import BaseUseCase


@dataclass(slots=True)
class AskFollowupUseCase(BaseUseCase[str, str]):
    oral_exam_service: OralExamService

    async def run(self, data: str) -> str:
        return await self.oral_exam_service.ask_followup(data)
