from dataclasses import dataclass

from pilot_coach.application.services.progress_service import ProgressService
from pilot_coach.shared.template import BaseUseCase


@dataclass(slots=True)
class GetProgressUseCase(BaseUseCase[str, dict]):
    progress_service: ProgressService

    async def run(self, data: str) -> dict:
        return await self.progress_service.get_progress(data)
