# 0002 — pgvector for MVP, not managed vector DB

**Status:** accepted
**Date:** 2026-05-03

## Context

We need a vector database for FAA chunk retrieval. Options considered:

| Option | Type | Notes |
|---|---|---|
| pgvector | Postgres extension | Single-DB simplicity, free, good metadata joins |
| Pinecone | Managed service | Fast, scalable, vendor cost |
| Weaviate | Managed or self-hosted | Hybrid search built-in |
| Qdrant | Managed or self-hosted | Strong filtering, open source |
| Chroma | Local-first | Great for prototyping, weak for production |

We already need Postgres for users, sessions, attempts, mastery, and source document metadata.

## Decision

Use **pgvector on the same Postgres instance** that holds relational data, for MVP.

## Consequences

**Good:**
- One database to operate, back up, and reason about
- Metadata joins are SQL — `WHERE certificate = 'IR' AND acs_task_code = 'II.A'` is trivial
- No additional vendor cost or API rate limits
- Migration to a dedicated vector DB later is straightforward — chunks + embeddings export to JSONL
- Postgres `tsvector` provides BM25-style keyword search in the same DB → enables hybrid search without a second service

**Bad / requires care:**
- pgvector performance tuning (index type: IVFFlat vs HNSW; ef_search) is on us
- At >1M chunks or high QPS, we may need to migrate
- Less ecosystem polish than Pinecone (no managed retraining, no built-in reranking)

## Alternatives considered

- **Pinecone** — chosen against because it adds a vendor + a separate metadata store. Reconsider if we exceed pgvector's comfortable scale (rough threshold: 1M+ chunks, sustained >100 QPS retrieval).
- **Weaviate** — hybrid search is attractive but adds infra. Postgres `tsvector` + pgvector covers the same ground for MVP.
- **Qdrant** — strong product, but same "second service to run" problem as Weaviate without compensating advantage at our scale.

## Migration trigger

Revisit this ADR when any of the following are true:
- Chunk count exceeds 1M
- p95 retrieval latency exceeds 500ms with HNSW indexing
- Hybrid search via `tsvector` proves insufficient for FAR/AIM lookups (eval set top-5 recall < 0.85 on regulatory queries)
