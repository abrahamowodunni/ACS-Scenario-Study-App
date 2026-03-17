from fastapi import APIRouter, Depends

from apps.api.dependencies import get_evaluation_service
from pilot_coach.application.dto.evaluation_request import EvaluationRequest
from pilot_coach.application.dto.evaluation_response import EvaluationResponse
from pilot_coach.application.services.evaluation_service import EvaluationService

router = APIRouter(prefix="/evaluation", tags=["evaluation"])


@router.post("/answer", response_model=EvaluationResponse)
async def evaluate_answer(
    request: EvaluationRequest,
    service: EvaluationService = Depends(get_evaluation_service),
) -> EvaluationResponse:
    return await service.evaluate(request)
