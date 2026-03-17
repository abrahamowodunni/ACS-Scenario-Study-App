from collections.abc import Sequence

from pilot_coach.domain.ports.vector_store_port import VectorStorePort
from pilot_coach.shared.settings import settings

try:
    from pinecone import Pinecone
except Exception:  # pragma: no cover - import guard for local bootstrap
    Pinecone = None


class PineconeStore(VectorStorePort):
    def __init__(self) -> None:
        self._enabled = bool(settings.pinecone_api_key and settings.pinecone_index_name and Pinecone)
        self.namespace = settings.pinecone_namespace
        self.index_name = settings.pinecone_index_name
        self.client = Pinecone(api_key=settings.pinecone_api_key) if self._enabled else None
        self.index = self.client.Index(self.index_name) if self._enabled else None

    async def similarity_search(
        self,
        query: str,
        top_k: int = 5,
        filter: dict | None = None,
    ) -> list[dict]:
        # Starter fallback so the scaffold runs before Pinecone is wired.
        if not self._enabled:
            return [
                {
                    "page_content": (
                        "The applicant demonstrates understanding of pilot qualifications, "
                        "documents, and required currency relevant to the operation."
                    ),
                    "metadata": {
                        "source_title": "Private Pilot Airplane ACS",
                        "section": "Area I - Preflight Preparation",
                        "page": 9,
                        "acs_code": "PA.I.A.K1",
                        "certificate_type": "private_pilot_airplane",
                    },
                },
                {
                    "page_content": (
                        "Aeronautical decision-making should account for personal minimums, "
                        "weather, aircraft limitations, and external pressures."
                    ),
                    "metadata": {
                        "source_title": "Risk Management Handbook",
                        "section": "Risk Management Fundamentals",
                        "page": 3,
                        "acs_code": "PA.I.A.R1",
                        "certificate_type": "private_pilot_airplane",
                    },
                },
            ]

        # Wire real search here once embeddings + index schema are in place.
        return []
