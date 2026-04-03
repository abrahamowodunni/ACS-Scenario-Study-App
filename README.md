# Pilot ACS Coach

A lightweight FAA ACS scenario study app scaffold with a **working simple RAG path** for local development.

## What is implemented now

- FastAPI API scaffold for scenario generation and answer evaluation.
- OpenAI provider with a fallback response when no key is configured.
- Pinecone vector store integration.
- **Local lexical vector store fallback** (zero cloud dependencies) that reads a seeded FAA-style corpus.
- A runnable notebook demo at `notebooks/simple_rag_demo.ipynb`.

## Quick start

```bash
uv sync
cp .env.example .env  # optional, only needed for OpenAI/Pinecone
uv run python -m apps.api.main
```

Open:
- API root: http://127.0.0.1:8000/
- Docs: http://127.0.0.1:8000/docs

## Local simple RAG behavior

If Pinecone credentials are not configured, the app automatically falls back to:

- `LocalVectorStore` using `data/seed/faa_private_pilot_samples.json`
- Token-overlap retrieval for top-k context chunks
- Metadata filtering (for example by certificate type)

This gives you an end-to-end local prototype while you iterate prompts and guardrails.

## Notebook demo

Use this notebook to show RAG retrieval working in minutes:

- `notebooks/simple_rag_demo.ipynb`

Run with Jupyter in your environment after `uv sync`.

## Dev commands

```bash
uv sync
uv run ruff check .
uv run pytest
```

## Next suggested increments

1. Replace lexical retrieval with embedding retrieval in Pinecone.
2. Ground scenario outputs with explicit citations from retrieved chunks.
3. Add prompt guardrails for “study-only” mode and unsafe advice refusal.
4. Add ACS-specific rubrics for evaluation scoring.
