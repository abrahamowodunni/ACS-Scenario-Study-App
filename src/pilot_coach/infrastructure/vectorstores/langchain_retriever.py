from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from pilot_coach.shared.settings import settings


class LangChainRetrieverFactory:
    def build(self, index) -> PineconeVectorStore:
        embeddings = OpenAIEmbeddings(
            model=settings.openai_embedding_model,
            api_key=settings.openai_api_key,
        )
        return PineconeVectorStore(
            index=index,
            embedding=embeddings,
            namespace=settings.pinecone_namespace,
        )
