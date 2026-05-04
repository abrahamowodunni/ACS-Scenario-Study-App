# ACS Scenario Study App — Documentation

Working brief for the FAA ACS AI Study App. Organized so a junior dev + Claude Code can navigate it without losing the thread.

## How to read this tree

- **Top-down:** [00-product/](00-product/) (the why) → [01-architecture/](01-architecture/) (how it fits) → drill into specific layers.
- **Bottom-up (current focus):** the **ingestion slice**. Read [04-data/](04-data/) then [05-ai-logic/rag-flow.md](05-ai-logic/rag-flow.md). This is what we build first.
- **Decisions:** every locked choice has a one-page ADR in [09-decisions/](09-decisions/). When something feels arbitrary, an ADR explains why.

## Locked decisions (as of 2026-05-03)

| Choice | Value | ADR |
|---|---|---|
| MVP wedge | Instrument Rating | [0005](09-decisions/0005-ir-first-wedge.md) |
| Architecture | RAG (not fine-tuning) | [0001](09-decisions/0001-rag-not-finetuning.md) |
| Backend | Python / FastAPI | [0003](09-decisions/0003-python-backend.md) |
| LLM | Claude — Sonnet generate, Haiku grade/validate | [0004](09-decisions/0004-claude-as-llm.md) |
| Vector DB | pgvector on Postgres | [0002](09-decisions/0002-pgvector-not-pinecone.md) |
| Frontend | Next.js + Tailwind + shadcn/ui | — |
| Embeddings | voyage-3 *(confirm during ingestion build)* | — |

## Folder map

| Folder | What lives here | Priority |
|---|---|---|
| [00-product/](00-product/) | Vision, personas, success metrics, roadmap | Reference |
| [01-architecture/](01-architecture/) | System overview, data flow, tech stack, NFRs | **P0** |
| [02-backend/](02-backend/) | FastAPI services, data models, auth, errors | **P0** for slice |
| [03-frontend/](03-frontend/) | Next.js architecture, components, screens | P1 |
| [04-data/](04-data/) | FAA sources, ingestion pipeline, chunking, metadata | **P0** ⭐ |
| [05-ai-logic/](05-ai-logic/) | RAG flow, prompts, guardrails, eval harness | **P0** ⭐ |
| [06-infra/](06-infra/) | Environments, hosting, secrets, CI/CD, cost | P1 |
| [07-ops/](07-ops/) | Monitoring, SME review, incident response | P2 |
| [08-testing/](08-testing/) | Test strategy, eval sets, manual QA | P1 |
| [09-decisions/](09-decisions/) | ADRs — one page each, "why this, not that" | **P0** |
| [10-glossary/](10-glossary/) | Shared vocabulary | Reference |

## Predecessor drafts

The two long-form drafts in this folder ([`faa_acs_ai_study_app_spec_v0_1.md`](faa_acs_ai_study_app_spec_v0_1.md) and [`faa-acs-study-app-spec-v0.1.md`](faa-acs-study-app-spec-v0.1.md)) are source material for this tree. They will be progressively split into the folders above. Treat them as historical context — once a folder doc exists for a topic, **that** doc is canonical.

## Document template (P0 docs)

1. **Purpose** — 1–2 sentences
2. **Contract** — the interface, schema, or behavior locked down
3. **Implementation notes** — how, with rationale
4. **Examples** — input → output
5. **Edge cases / what to avoid**
6. **Open questions**

P1+ docs may be stubs until they need to be filled.

## Status legend

- **locked** — decided; change requires an ADR update
- **draft** — content present, open for edit
- **stub** — placeholder; fill when the slice that needs it lands
- **TBD** — not yet started
