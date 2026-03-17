from abc import ABC, abstractmethod


class PromptRepositoryPort(ABC):
    @abstractmethod
    def load_prompt(self, name: str) -> str:
        raise NotImplementedError
