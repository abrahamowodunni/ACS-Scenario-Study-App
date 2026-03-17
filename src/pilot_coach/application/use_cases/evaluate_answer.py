from dataclasses import dataclass

from pilot_coach.application.dto.evaluation_request import EvaluationRequest
from pilot_coach.application.dto.evaluation_response import EvaluationResponse
from pilot_coach.application.services.evaluation_service import EvaluationService
from pilot_coach.shared.template import BaseUseCase


@dataclass(slots=True)
class EvaluateAnswerUseCase(BaseUseCase[EvaluationRequest, EvaluationResponse]):
    evaluation_service: EvaluationService

    async def run(self, data: EvaluationRequest) -> EvaluationResponse:
        return await self.evaluation_service.evaluate(data)
