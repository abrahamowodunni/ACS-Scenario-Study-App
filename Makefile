.PHONY: venv run dev lint test

PROJECT_NAME := $(shell grep '^name = ' pyproject.toml | head -1 | sed 's/name = "\(.*\)"/\1/')

venv:
	uv venv $(PROJECT_NAME)
	@echo "Activate with: source $(PROJECT_NAME)/bin/activate"

run:
	uv run python -m apps.api.main

dev:
	uv run uvicorn apps.api.main:app --reload

lint:
	uv run ruff check .

test:
	uv run pytest
