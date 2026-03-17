from pilot_coach.application.dto.scenario_request import ScenarioRequest
from pilot_coach.application.dto.scenario_response import ScenarioResponse
from pilot_coach.application.services.citation_service import CitationService
from pilot_coach.application.services.retrieval_service import RetrievalService
from pilot_coach.domain.ports.llm_port import LLMPort
from pilot_coach.shared.utils import join_nonempty


class ScenarioService:
    def __init__(
        self,
        llm: LLMPort,
        retrieval_service: RetrievalService,
        citation_service: CitationService,
    ) -> None:
        self.llm = llm
        self.retrieval_service = retrieval_service
        self.citation_service = citation_service

    async def generate(self, request: ScenarioRequest) -> ScenarioResponse:
        docs = await self.retrieval_service.get_context(
            query=f"{request.task_code} {request.task_title}",
            top_k=4,
            filter={"certificate_type": request.certificate_type.value},
        )
        citations = self.citation_service.build_citations(docs)

        if not docs:
            return ScenarioResponse(
                title=f"{request.task_code} Mock Scenario",
                scenario=(
                    "You are preparing for your checkride and the examiner asks you to explain "
                    f"{request.task_title} in a practical preflight situation."
                ),
                follow_up_question="What risks would you identify before the flight begins?",
                citations=[],
            )

        context_preview = "\n".join(doc["page_content"] for doc in docs[:3])
        prompt = join_nonempty(
            [
                "You are an FAA-grounded ACS study coach.",
                f"Generate a realistic scenario for task {request.task_code}: {request.task_title}.",
                f"Difficulty: {request.difficulty}.",
                "Keep it study-focused and concise.",
                f"Context:\n{context_preview}",
            ],
            sep="\n\n",
        )
        text = await self.llm.generate_text(prompt)
        return ScenarioResponse(
            title=f"{request.task_code} Scenario",
            scenario=text,
            follow_up_question="What would be your first decision and why?",
            citations=citations,
        )
