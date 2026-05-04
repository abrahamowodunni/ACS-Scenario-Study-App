# 0001 — RAG, not fine-tuning

**Status:** accepted
**Date:** 2026-05-03

## Context

The product's value depends on generating accurate, FAA-grounded study questions and explanations. There are three plausible architectures:

1. **RAG** — retrieve relevant FAA chunks at query time, generate from them
2. **Fine-tuning** — train a model on FAA-aligned Q&A pairs
3. **Prompt-stuffing** — paste FAA docs into the context window directly

FAA materials are large (thousands of pages), authoritative, and updated on a regular cycle (ACS revisions, CFR amendments, AIM cycle ~every 6 months). Citation traceability is non-negotiable — users (and SMEs) must be able to verify any claim back to a specific FAA source.

## Decision

Use **RAG with metadata-filtered retrieval** as the core architecture.

## Consequences

**Good:**
- Citations are natural — the retrieved chunk *is* the source
- Document updates re-index, no retraining needed
- ACS metadata (Area → Task → Element) maps cleanly to vector DB filters
- Vendor-flexible — we can swap LLMs without losing the corpus
- "Answer only from context" prompting is the strongest hallucination mitigation available without custom training

**Bad / requires care:**
- Retrieval quality is now the bottleneck — bad chunks → bad answers
- Chunking strategy is load-bearing (see [04-data/chunking-strategy.md](../04-data/chunking-strategy.md))
- More moving parts than a static prompt: ingestion pipeline, vector DB, retriever, validator
- Citation validation requires a separate LLM pass

## Alternatives considered

- **Fine-tuning:** doesn't guarantee factual correctness, locks the model to a snapshot, can't produce citations naturally, expensive to refresh on FAA updates. May revisit in Phase 2 for *style/format consistency* (not facts) once we have an eval set.
- **Prompt-stuffing:** doesn't scale past a few documents; cost and latency grow with context size; can't filter by ACS metadata.
- **Agentic retrieval (LLM iteratively searches):** higher latency, higher cost, harder to evaluate. Defer to Phase 2 for complex multi-hop scenario questions.
