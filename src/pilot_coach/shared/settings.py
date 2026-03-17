from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Pilot ACS Coach API"
    app_env: str = "local"
    app_host: str = "127.0.0.1"
    app_port: int = 8000

    openai_api_key: str = ""
    openai_model: str = "gpt-5"
    openai_embedding_model: str = "text-embedding-3-large"

    pinecone_api_key: str = ""
    pinecone_index_name: str = "pilot-acs-index"
    pinecone_namespace: str = "private-pilot"

    sqlite_url: str = "sqlite+aiosqlite:///./pilot_coach.db"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
