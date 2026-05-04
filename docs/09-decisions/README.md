# 09 — Architecture Decision Records

Each ADR is one page. Format: **Context → Decision → Consequences**.

## Why ADRs

Six weeks from now, when Claude Code (or an investor, or future-you) asks "why pgvector and not Pinecone?" — the answer should be a one-page doc, not "I don't remember."

ADRs are tiny by design. If yours is over a page, you're writing a spec, not an ADR.

## Index

| # | Title | Status | Date |
|---|---|---|---|
| [0001](0001-rag-not-finetuning.md) | RAG, not fine-tuning | accepted | 2026-05-03 |
| [0002](0002-pgvector-not-pinecone.md) | pgvector for MVP, not managed vector DB | accepted | 2026-05-03 |
| [0003](0003-python-backend.md) | Python / FastAPI backend | accepted | 2026-05-03 |
| [0004](0004-claude-as-llm.md) | Claude as LLM provider (Sonnet + Haiku) | accepted | 2026-05-03 |
| [0005](0005-ir-first-wedge.md) | Instrument Rating as MVP wedge | accepted | 2026-05-03 |

## When to write a new ADR

- Locking a stack choice that has multiple defensible options
- Reversing a previous ADR (write a new one, mark the old one "superseded by 000X")
- Choosing a non-obvious approach where future-you will ask "why?"

## When NOT to write an ADR

- Implementation details (which library function to use)
- Style/formatting choices
- Anything that's a one-way door regardless (e.g., "use the FAA's actual document titles")

## Template

```markdown
# 000X — Title

**Status:** proposed | accepted | superseded by 000Y
**Date:** YYYY-MM-DD

## Context
What's the situation? What forces are at play?

## Decision
What did we decide?

## Consequences
What follows from this — good and bad? What's now harder, what's now easier?

## Alternatives considered
Briefly: what else, and why not.
```
