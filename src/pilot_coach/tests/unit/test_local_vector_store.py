import pytest

from pilot_coach.infrastructure.vectorstores.local_store import LocalVectorStore


@pytest.mark.asyncio
async def test_similarity_search_returns_ranked_docs() -> None:
    store = LocalVectorStore()

    results = await store.similarity_search(
        query="weather briefing and cross-country planning",
        top_k=2,
        filter={"certificate_type": "private_pilot_airplane"},
    )

    assert len(results) == 2
    assert all(result["metadata"]["certificate_type"] == "private_pilot_airplane" for result in results)
    assert any("weather" in result["page_content"].lower() for result in results)
