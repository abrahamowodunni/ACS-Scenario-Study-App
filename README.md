# Pilot ACS Coach Scaffold

A modular Python scaffold for a scenario-based FAA ACS study coach.

## Stack

- Python 3.11+
- `uv` for dependency management
- FastAPI for the API
- OpenAI for generation
- Pinecone for vector storage
- LangChain as a thin integration layer
- SQLite for local session/progress metadata

## Quick start

```bash
uv sync
cp .env.example .env
uv run python -m apps.api.main
```

Open:
- API root: http://127.0.0.1:8000/
- Docs: http://127.0.0.1:8000/docs

## Dev commands

```bash
uv sync
uv run ruff check .
uv run pytest
uv run python scripts/scaffold_module.py src/pilot_coach/application/use_cases GenerateScenarioUseCase
```

## Project notes

- `domain/` holds business concepts and ports only.
- `application/` holds use cases and orchestration services.
- `infrastructure/` holds OpenAI, Pinecone, LangChain, SQLite, parsing.
- `prompts/` stores prompt assets outside code.
- `shared/template.py` gives you a reusable pattern for new modules.
- `scripts/scaffold_module.py` creates starter modules fast.

## First endpoints

- `GET /health`
- `POST /scenarios/generate`
- `POST /evaluation/answer`
- `GET /progress/{user_id}`

The runtime is intentionally lightweight. `GET /health` works immediately. The scenario and evaluation routes are scaffolded and ready for you to deepen.
