from openai import AsyncOpenAI

from pilot_coach.domain.ports.llm_port import LLMPort
from pilot_coach.shared.settings import settings


class OpenAIProvider(LLMPort):
    def __init__(self) -> None:
        self._enabled = bool(settings.openai_api_key)
        self.client = AsyncOpenAI(api_key=settings.openai_api_key) if self._enabled else None
        self.model = settings.openai_model

    async def generate_text(self, prompt: str) -> str:
        if not self._enabled:
            return (
                "You are planning a daytime cross-country flight. During preflight, your examiner "
                "tells you ceilings may lower near your destination and asks how you would assess "
                "whether the flight is still safe and legal."
            )

        response = await self.client.responses.create(
            model=self.model,
            input=prompt,
            text={"verbosity": "medium"},
        )
        return response.output_text

    async def generate_structured(self, prompt: str, schema):
        if not self._enabled:
            return schema(
                title="Mock Scenario",
                scenario="This is a mock scenario generated because OPENAI_API_KEY is not configured.",
                follow_up_question="What would you check first?",
            )

        response = await self.client.responses.parse(
            model=self.model,
            input=prompt,
            text_format=schema,
        )
        return response.output_parsed
