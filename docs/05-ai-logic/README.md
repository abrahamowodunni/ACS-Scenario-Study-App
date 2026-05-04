# 05 — AI Logic ⭐

RAG flow, prompts, guardrails, evaluation. The brain of the system.

## Files

| File | Purpose | Status | Priority |
|---|---|---|---|
| `rag-flow.md` | Retrieval logic: query analysis, filters, top-k, reranking, validator | stub | **P0** |
| `guardrails.md` | Hallucination defenses, refusal paths, citation roundtrip | stub | **P0** |
| `eval-harness.md` | How we test prompt + retrieval changes (golden set, metrics) | stub | P1 |
| [`prompts/`](prompts/) | One file per prompt, version-controlled | stub | **P0** |

## Why prompts get their own folder

Prompts are code. They need version control, review, and regression testing the same way a function does. Inline strings buried in services rot fast and can't be diffed.

## Sources

- [`../faa-acs-study-app-spec-v0.1.md`](../faa-acs-study-app-spec-v0.1.md) §3.4 (data flow), §5 (prompt strategy + guardrails)
- [`../faa_acs_ai_study_app_spec_v0_1.md`](../faa_acs_ai_study_app_spec_v0_1.md) §5 (longer prompt templates)
