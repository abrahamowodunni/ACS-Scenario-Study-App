from pilot_coach.domain.ports.vector_store_port import VectorStorePort


class RetrievalService:
    def __init__(self, vector_store: VectorStorePort) -> None:
        self.vector_store = vector_store

    async def get_context(self, query: str, top_k: int = 5, filter: dict | None = None) -> list[dict]:
        results = await self.vector_store.similarity_search(query=query, top_k=top_k, filter=filter)
        return results
