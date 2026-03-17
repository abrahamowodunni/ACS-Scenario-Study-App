from dataclasses import dataclass

from pilot_coach.application.dto.scenario_request import ScenarioRequest
from pilot_coach.application.dto.scenario_response import ScenarioResponse
from pilot_coach.application.services.scenario_service import ScenarioService
from pilot_coach.shared.template import BaseUseCase


@dataclass(slots=True)
class GenerateScenarioUseCase(BaseUseCase[ScenarioRequest, ScenarioResponse]):
    scenario_service: ScenarioService

    async def validate(self, data: ScenarioRequest) -> None:
        if not data.task_code:
            raise ValueError("task_code is required")

    async def run(self, data: ScenarioRequest) -> ScenarioResponse:
        return await self.scenario_service.generate(data)
