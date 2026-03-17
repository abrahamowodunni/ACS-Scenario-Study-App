from pinecone import Pinecone, ServerlessSpec

from pilot_coach.shared.settings import settings


def main() -> None:
    if not settings.pinecone_api_key:
        raise RuntimeError("Set PINECONE_API_KEY first.")

    pc = Pinecone(api_key=settings.pinecone_api_key)
    existing = [index["name"] for index in pc.list_indexes()]

    if settings.pinecone_index_name in existing:
        print(f"Index {settings.pinecone_index_name} already exists.")
        return

    pc.create_index(
        name=settings.pinecone_index_name,
        dimension=3072,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    print(f"Created index {settings.pinecone_index_name}")


if __name__ == "__main__":
    main()
