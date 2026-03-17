from abc import ABC, abstractmethod


class SessionRepositoryPort(ABC):
    @abstractmethod
    async def get_progress(self, user_id: str) -> dict:
        raise NotImplementedError
