# 0004 — Claude as LLM provider (Sonnet + Haiku)

**Status:** accepted
**Date:** 2026-05-03

## Context

Two LLM roles in the system:

1. **Generation** — produce ACS-aligned questions, scenarios, explanations. Must follow strict JSON output, cite retrieved chunks, refuse when context is insufficient.
2. **Grading + validation** — grade free-response answers against a rubric; verify generated questions cite real chunks and don't hallucinate.

These have different cost/quality requirements. Generation needs the strongest reasoning; grading/validation can use a cheaper, faster model.

## Decision

Use **Claude — Sonnet for generation, Haiku for grading and validator passes.**

## Consequences

**Good:**
- Strong instruction-following and JSON discipline (important for our strict output schemas)
- Long context window — we can fit retrieved chunks + ACS task definitions + few-shot examples comfortably
- Citation behavior is reliable — Claude is good at quoting from provided context rather than inventing
- Two-tier (Sonnet/Haiku) gives natural cost optimization: ~10x cheaper validator passes
- Single vendor → single SDK, single billing relationship, simpler ops

**Bad / requires care:**
- Vendor lock-in (mitigated: prompts are version-controlled separately from code; swapping providers is a finite project, not a rewrite)
- Anthropic API outages = product outage. Need a degraded mode (cached questions, no live generation) for incident response.
- Pricing changes are a business risk — track per-question cost and set alerts

## Alternatives considered

- **OpenAI GPT-4-class** — comparable quality. Reconsider if Claude pricing or availability becomes a problem.
- **Open-source (Llama 3.1 70B+) via Together/Fireworks/Groq** — defer until cost forces it. Self-hosting is premature optimization.
- **Mixed providers** (Claude generate + GPT-4 grade) — adds vendor complexity for marginal benefit. Keep it simple at MVP.

## Cost levers to pull as scale grows

1. Cache generated questions by `(acs_task, retrieved_chunk_ids_hash)` → hits avoid generation entirely
2. Move easy question types (knowledge recall) to Haiku
3. Validator runs only on Sonnet outputs (Haiku grading bypasses double-grading)
4. Pre-generate a question bank for high-traffic ACS tasks; live generation only for weak-area drilling

## Open questions

- Confirm exact Claude model IDs at implementation time (Sonnet and Haiku families update); pin in [01-architecture/tech-stack.md](../01-architecture/tech-stack.md).
- Decide on prompt caching strategy (Anthropic supports prompt caching; system prompts + few-shot examples are good cache candidates).
