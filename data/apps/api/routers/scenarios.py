from fastapi import APIRouter, Depends

from apps.api.dependencies import get_scenario_service
from pilot_coach.application.dto.scenario_request import ScenarioRequest
from pilot_coach.application.dto.scenario_response import ScenarioResponse
from pilot_coach.application.services.scenario_service import ScenarioService

router = APIRouter(prefix="/scenarios", tags=["scenarios"])


@router.post("/generate", response_model=ScenarioResponse)
async def generate_scenario(
    request: ScenarioRequest,
    service: ScenarioService = Depends(get_scenario_service),
) -> ScenarioResponse:
    return await service.generate(request)
