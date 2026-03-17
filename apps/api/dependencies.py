from functools import lru_cache

from pilot_coach.application.services.citation_service import CitationService
from pilot_coach.application.services.evaluation_service import EvaluationService
from pilot_coach.application.services.progress_service import ProgressService
from pilot_coach.application.services.retrieval_service import RetrievalService
from pilot_coach.application.services.scenario_service import ScenarioService
from pilot_coach.infrastructure.repositories.sqlite_session_repository import SQLiteSessionRepository
from pilot_coach.infrastructure.vectorstores.pinecone_store import PineconeStore
from pilot_coach.infrastructure.llm.openai_provider import OpenAIProvider


@lru_cache
def get_llm_provider() -> OpenAIProvider:
    return OpenAIProvider()


@lru_cache
def get_vector_store() -> PineconeStore:
    return PineconeStore()


@lru_cache
def get_session_repository() -> SQLiteSessionRepository:
    return SQLiteSessionRepository()


def get_retrieval_service() -> RetrievalService:
    return RetrievalService(vector_store=get_vector_store())


def get_citation_service() -> CitationService:
    return CitationService()


def get_scenario_service() -> ScenarioService:
    return ScenarioService(
        llm=get_llm_provider(),
        retrieval_service=get_retrieval_service(),
        citation_service=get_citation_service(),
    )


def get_evaluation_service() -> EvaluationService:
    return EvaluationService(
        llm=get_llm_provider(),
        retrieval_service=get_retrieval_service(),
    )


def get_progress_service() -> ProgressService:
    return ProgressService(session_repository=get_session_repository())
