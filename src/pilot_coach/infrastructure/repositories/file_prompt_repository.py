from pathlib import Path

from pilot_coach.domain.ports.prompt_repository_port import PromptRepositoryPort


class FilePromptRepository(PromptRepositoryPort):
    def __init__(self, base_path: str = "src/pilot_coach/prompts") -> None:
        self.base_path = Path(base_path)

    def load_prompt(self, name: str) -> str:
        target = self.base_path / name
        return target.read_text(encoding="utf-8")
