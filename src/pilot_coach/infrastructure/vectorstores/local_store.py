from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from pilot_coach.domain.ports.vector_store_port import VectorStorePort

TOKEN_PATTERN = re.compile(r"[a-z0-9]+")


class LocalVectorStore(VectorStorePort):
    """Tiny lexical retriever for local development and notebook demos."""

    def __init__(self, corpus_path: str = "data/seed/faa_private_pilot_samples.json") -> None:
        self.corpus_path = Path(corpus_path)
        self.documents = self._load_documents()

    async def similarity_search(
        self,
        query: str,
        top_k: int = 5,
        filter: dict | None = None,
    ) -> list[dict[str, Any]]:
        query_tokens = set(TOKEN_PATTERN.findall(query.lower()))
        scored: list[tuple[int, dict[str, Any]]] = []

        for doc in self.documents:
            metadata = doc.get("metadata", {})
            if filter and any(metadata.get(key) != value for key, value in filter.items()):
                continue

            text_tokens = set(TOKEN_PATTERN.findall(doc.get("page_content", "").lower()))
            overlap = len(query_tokens.intersection(text_tokens))
            if overlap > 0:
                scored.append((overlap, doc))

        scored.sort(key=lambda item: item[0], reverse=True)

        if scored:
            return [doc for _, doc in scored[:top_k]]

        return self.documents[:top_k]

    def _load_documents(self) -> list[dict[str, Any]]:
        if not self.corpus_path.exists():
            return []

        with self.corpus_path.open("r", encoding="utf-8") as f:
            payload = json.load(f)

        if not isinstance(payload, list):
            return []

        return [doc for doc in payload if isinstance(doc, dict)]
