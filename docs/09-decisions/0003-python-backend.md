# 0003 — Python / FastAPI backend

**Status:** accepted
**Date:** 2026-05-03

## Context

The backend needs to handle: ingestion (PDF parsing, chunking, embedding), retrieval (pgvector queries, metadata filtering), LLM orchestration (Claude API, prompt assembly, validation), and the application API (auth, sessions, mastery tracking).

Two language candidates:

- **Python (FastAPI)** — strongest AI/ML ecosystem (PyMuPDF, pdfplumber, unstructured, Anthropic SDK, eval tooling like Braintrust/Langfuse, evaluation libraries)
- **TypeScript (Node + Fastify or Next.js API routes)** — full-stack TS consistency with the Next.js frontend, slightly faster solo-dev iteration if the developer is already TS-fluent

## Decision

Use **Python 3.12 + FastAPI**.

## Consequences

**Good:**
- Best-in-class libraries for every step of the ingestion pipeline
- Anthropic SDK and embedding clients are first-class in Python
- Pydantic for request/response validation and chunk metadata schemas
- Eval harness tooling (Braintrust, Langfuse, Ragas) has strongest Python support
- Developer is Python-fluent → faster shipping

**Bad / requires care:**
- Two languages in the codebase (Python backend + TypeScript frontend) → two deploy pipelines, two dependency management systems
- Type sharing between backend and frontend requires either OpenAPI codegen or hand-maintained TypeScript types
- Slightly higher operational overhead than a single-language stack

## Alternatives considered

- **TypeScript (Node + Fastify)** — would unify the stack but pushes against developer fluency. Anthropic and embedding SDKs are good in TS but the AI/eval ecosystem is weaker. Reconsider only if Python becomes a hiring or operational pain point.
- **Next.js API routes only** — too coupled; ingestion jobs and long-running pipelines don't fit serverless API routes well.

## Implementation notes

- Use **Pydantic v2** for all schemas — chunk metadata, request/response, LLM output validation
- Generate **OpenAPI spec** from FastAPI; generate TypeScript types from OpenAPI for the frontend
- Long-running ingestion jobs: start as scripts; move to a job queue (Celery + Redis, or Arq) only when needed
