# Tech Stack

**Status:** locked (2026-05-03)
**Owner:** TBD

## Purpose

Single source of truth for stack choices. Every component below is locked unless an ADR in [09-decisions/](../09-decisions/) supersedes it.

## Stack

| Layer | Choice | Why | ADR |
|---|---|---|---|
| **Frontend** | Next.js 14+ (App Router) + Tailwind + shadcn/ui | Fast solo-dev velocity, good DX, easy auth, Vercel deploy | — |
| **Backend** | Python 3.12 + FastAPI | Strong AI/RAG ecosystem; team is Python-fluent | [0003](../09-decisions/0003-python-backend.md) |
| **LLM — generation** | Claude Sonnet (latest) | Strong instruction-following, citation discipline, long context | [0004](../09-decisions/0004-claude-as-llm.md) |
| **LLM — grading + validator** | Claude Haiku (latest) | Cheap, fast, sufficient for rubric grading and citation checks | [0004](../09-decisions/0004-claude-as-llm.md) |
| **Embeddings** | `voyage-3` *(primary)*, OpenAI `text-embedding-3-large` *(fallback to benchmark)* | Strong on technical/regulatory text | TBD — confirm during ingestion build |
| **Vector DB** | pgvector on Postgres | Single-DB simplicity, free, good metadata joins | [0002](../09-decisions/0002-pgvector-not-pinecone.md) |
| **Relational DB** | Postgres 16+ | Same instance as pgvector — users, sessions, attempts, mastery | — |
| **Object storage** | S3-compatible (Cloudflare R2 or AWS S3) | Raw PDFs, parsed text, chunked JSONL, eval sets, doc snapshots | — |
| **Auth** | Clerk | Skip undifferentiated work; FastAPI integration via JWT | — |
| **Billing** | Stripe | Industry default; defer integration until Phase 1.5 | — |
| **Eval harness** | Custom + Braintrust *or* Langfuse | Track hallucination rate from day one | — |
| **Architecture** | RAG with metadata-filtered hybrid retrieval | Required for FAA-grounded citation | [0001](../09-decisions/0001-rag-not-finetuning.md) |

## Hosting (target)

- **Frontend:** Vercel
- **Backend:** Render or Fly.io (Python-friendly, persistent Postgres)
- **Postgres + pgvector:** managed (Neon, Supabase, or RDS) — must support pgvector extension
- **Object storage:** Cloudflare R2 (cheaper egress) or AWS S3

## Versions to pin (TBD during setup)

- Python: 3.12.x
- FastAPI: latest stable
- pgvector extension version
- Anthropic SDK version
- Embedding model + dimension count (versioned in chunk metadata — see [04-data/metadata-schema.md](../04-data/metadata-schema.md))

## What's deliberately NOT in the stack

- **LangChain / LlamaIndex** — too much abstraction overhead for the small surface area we need; we'll write the retrieval and prompt assembly directly.
- **Fine-tuned models** — see [ADR 0001](../09-decisions/0001-rag-not-finetuning.md). Reconsider in Phase 2 only with concrete eval evidence.
- **Self-hosted LLMs** — defer until unit economics demand it.
- **Mobile native** — PWA-first; revisit in Phase 3.

## Open questions

- Confirm voyage-3 vs OpenAI embeddings via head-to-head retrieval eval on FAA corpus (target: top-5 recall on a 50-question gold set).
- Reranker (cross-encoder) — Phase 1 or Phase 2? Default: Phase 2, unless retrieval eval shows MVP-blocking precision issues.
- BM25 / hybrid search — Postgres `tsvector` is built-in; confirm it's good enough vs. dedicated (Elastic, Weaviate built-in hybrid).
