from abc import ABC, abstractmethod
from typing import Any


class LLMPort(ABC):
    @abstractmethod
    async def generate_text(self, prompt: str) -> str:
        raise NotImplementedError

    @abstractmethod
    async def generate_structured(self, prompt: str, schema: Any) -> Any:
        raise NotImplementedError
