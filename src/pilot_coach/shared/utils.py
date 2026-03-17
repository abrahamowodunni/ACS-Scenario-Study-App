from __future__ import annotations

from pathlib import Path
from typing import Iterable


def ensure_directory(path: str | Path) -> Path:
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def snake_case(name: str) -> str:
    output = []
    for idx, char in enumerate(name):
        if char.isupper() and idx > 0:
            output.append("_")
        output.append(char.lower())
    return "".join(output)


def join_nonempty(parts: Iterable[str], sep: str = " | ") -> str:
    return sep.join(part for part in parts if part)
