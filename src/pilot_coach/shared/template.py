from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar


InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


class Executable(Protocol[InputT, OutputT]):
    async def execute(self, data: InputT) -> OutputT:
        ...


@dataclass(slots=True)
class BaseUseCase(Generic[InputT, OutputT]):
    name: str

    async def validate(self, data: InputT) -> None:
        """Override when input validation is needed."""
        return None

    async def run(self, data: InputT) -> OutputT:
        raise NotImplementedError("Subclasses must implement run().")

    async def execute(self, data: InputT) -> OutputT:
        await self.validate(data)
        return await self.run(data)
