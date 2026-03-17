from pilot_coach.application.dto.evaluation_request import EvaluationRequest
from pilot_coach.application.dto.evaluation_response import EvaluationResponse
from pilot_coach.application.services.retrieval_service import RetrievalService
from pilot_coach.domain.models.citation import Citation
from pilot_coach.domain.ports.llm_port import LLMPort


class EvaluationService:
    def __init__(self, llm: LLMPort, retrieval_service: RetrievalService) -> None:
        self.llm = llm
        self.retrieval_service = retrieval_service

    async def evaluate(self, request: EvaluationRequest) -> EvaluationResponse:
        docs = await self.retrieval_service.get_context(
            query=f"{request.task_code} {request.question}",
            top_k=3,
        )

        citations = [
            Citation(
                source_title=doc.get("metadata", {}).get("source_title", "FAA Source"),
                section=doc.get("metadata", {}).get("section"),
                page=doc.get("metadata", {}).get("page"),
                acs_code=doc.get("metadata", {}).get("acs_code"),
            )
            for doc in docs
        ]

        # Deliberately simple starter logic. Replace with rubric + model eval later.
        answer_lower = request.answer.lower()
        strengths = []
        gaps = []

        if "risk" in answer_lower or "weather" in answer_lower or "minimum" in answer_lower:
            strengths.append("You identified at least one operational risk factor.")
        else:
            gaps.append("Call out the key risks more explicitly.")

        if len(request.answer.split()) > 30:
            strengths.append("Your answer has useful detail.")
        else:
            gaps.append("Expand the answer with more detail and reasoning.")

        return EvaluationResponse(
            accuracy_score=0.7,
            risk_score=0.7 if strengths else 0.5,
            completeness_score=0.75 if len(request.answer.split()) > 30 else 0.5,
            strengths=strengths or ["You attempted a practical response to the scenario."],
            gaps=gaps or ["Tie your answer back to FAA guidance and ACS language."],
            next_step="Re-answer using one regulation, one risk, and one practical action.",
            citations=citations,
        )
