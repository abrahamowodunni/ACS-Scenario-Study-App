# 08 — Testing & Evaluation

Quality bar. Two kinds of tests:

- **Code correctness** — unit, integration, e2e (does the function do what the signature claims?)
- **Feature correctness** — eval sets (does the LLM produce a good answer?)

These are not the same thing and need different tooling.

## Files

| File | Purpose | Status | Priority |
|---|---|---|---|
| `test-strategy.md` | Unit / integration / e2e — what we test where | stub | P1 |
| `eval-sets.md` | Golden set for retrieval + generation regressions | stub | P1 |
| `manual-qa-checklist.md` | Pre-demo / pre-deploy checklist | stub | P1 |

## Eval set — the most important file in this folder

The eval set is the contract for "is the LLM doing its job?" Without it, prompt changes are vibes.

Target for MVP: **200+ SME-graded items**, structured as:

```json
{
  "id": "ir-eval-001",
  "acs_task": "II.A.K1",
  "question": "...",
  "ideal_answer": "...",
  "ideal_citations": ["14 CFR 91.167"],
  "min_chunks_in_top_k": ["chunk_id_1", "chunk_id_2"]
}
```

Run on every prompt change, every chunking change, every embedding model swap.
