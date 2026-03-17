from abc import ABC, abstractmethod
from typing import Any


class VectorStorePort(ABC):
    @abstractmethod
    async def similarity_search(self, query: str, top_k: int = 5, filter: dict | None = None) -> list[Any]:
        raise NotImplementedError
