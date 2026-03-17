.PHONY: run dev lint test

run:
	uv run python -m apps.api.main

dev:
	uv run uvicorn apps.api.main:app --reload

lint:
	uv run ruff check .

test:
	uv run pytest
