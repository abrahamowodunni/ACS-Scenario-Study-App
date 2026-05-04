# 10 — Glossary

Shared vocabulary. When a term appears more than once across the docs, it lives here.

## Aviation

- **ACS** — Airman Certification Standards. The FAA document defining what a candidate must know, do, and manage for a given certificate.
- **Area of Operation** — top-level grouping in the ACS (e.g., "Preflight Preparation").
- **Task** — subdivision of an Area of Operation (e.g., "Pilot Qualifications" within Preflight Preparation).
- **Element** — atomic knowledge / risk / skill item within a Task. Coded like `II.A.K1` (Area II, Task A, Knowledge element 1).
- **DPE** — Designated Pilot Examiner. Conducts checkrides on the FAA's behalf.
- **CFI** — Certified Flight Instructor. **CFII** — Certified Flight Instructor, Instrument.
- **Checkride** — practical test for a certificate or rating. Includes oral exam + flight portion.
- **Oral exam** — the verbal questioning portion of the checkride. The part our app most directly prepares users for.
- **PPL** — Private Pilot License. **IR** — Instrument Rating.
- **PHAK** — Pilot's Handbook of Aeronautical Knowledge (FAA-H-8083-25).
- **IFH** — Instrument Flying Handbook (FAA-H-8083-15).
- **IPH** — Instrument Procedures Handbook (FAA-H-8083-16).
- **AIM** — Aeronautical Information Manual.
- **FAR / 14 CFR** — Federal Aviation Regulations, codified in Title 14 of the Code of Federal Regulations. Part 61 = certification; Part 91 = general operating rules.
- **PAVE / IMSAFE / 5P / DECIDE** — risk-management mnemonics taught in the ACS.

## Technical

- **RAG** — Retrieval-Augmented Generation. See [09-decisions/0001-rag-not-finetuning.md](../09-decisions/0001-rag-not-finetuning.md).
- **Chunk** — a unit of source text indexed for retrieval. Chunking rules: [04-data/chunking-strategy.md](../04-data/chunking-strategy.md).
- **Hybrid search** — combining dense (vector) and sparse (keyword/BM25) retrieval.
- **Reranker** — a cross-encoder model that re-scores top-k retrieved chunks for higher precision. Phase 2 candidate.
- **Validator** — the LLM-as-judge pass that checks generated output cites real chunks and doesn't hallucinate. See [05-ai-logic/guardrails.md](../05-ai-logic/guardrails.md).
- **Eval set** — gold-standard Q&A pairs for regression testing. See [08-testing/eval-sets.md](../08-testing/eval-sets.md).
- **ADR** — Architecture Decision Record. One-page "why this, not that." See [09-decisions/](../09-decisions/).

## Product

- **Wedge** — the focused initial use case we ship first. For us: IR candidates preparing for the oral portion of the checkride. See [09-decisions/0005-ir-first-wedge.md](../09-decisions/0005-ir-first-wedge.md).
- **Mastery score** — per-ACS-task tracking of user performance. Drives adaptive question selection.
- **Weak area** — an ACS task where the user's mastery score is below threshold. Adaptive selection biases toward these.
