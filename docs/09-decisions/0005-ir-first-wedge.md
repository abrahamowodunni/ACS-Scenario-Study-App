# 0005 — Instrument Rating as MVP wedge

**Status:** accepted
**Date:** 2026-05-03

## Context

We can't launch with full FAA ACS coverage. We need to pick one certificate/rating to ingest, prompt-engineer, eval, and SME-review first. Candidates:

- **Private Pilot Airplane (PPL)** — largest pool of candidates, lowest price tolerance, broad ACS surface area
- **Instrument Rating (IR)** — second-stage pilots, higher willingness to pay, dense regulatory material
- **Commercial / CFI** — smaller audience, high price tolerance, niche

## Decision

Build the MVP for **Instrument Rating candidates**.

## Consequences

**Good:**
- IR oral exams are dense in regs, approach plates, weather products, and decision-making — exactly the surface area where RAG produces the biggest lift over generic ChatGPT
- IR candidates already pay for training (CFII time is expensive) — willingness to pay is established
- Smaller candidate pool means faster SME network bootstrap (a handful of CFIIs can review the eval set)
- Tier-1 IR document set (ACS-8B, IFH, IPH, AIM, FAR 91 subset) is bounded and well-defined
- Demonstrating quality on dense regulatory content is a stronger investor proof point than easy PPL recall

**Bad / requires care:**
- Smaller TAM than PPL → revenue ramp is slower
- IR candidates are already pilots → they will spot subtle errors more reliably (good for quality, bad if quality is shaky)
- Approach plate / chart visual reasoning is out of scope for text-only RAG; need to scope around or document as a known limitation

## Alternatives considered

- **PPL first** — tempting for TAM, but the wedge argument is weaker: lots of PPL prep is rote written-test memorization, where existing tools (Sheppard Air) are entrenched and good. RAG advantage is smaller for definitions/recall than for regulatory reasoning.
- **CFI first** — too niche for an MVP. Revisit in Phase 3.

## Phase progression

- **MVP:** IR only, full Tier-1 doc coverage
- **Phase 2:** add PPL once IR is stable and eval is mature
- **Phase 3+:** Commercial, CFI, recurrent

## Open questions

- Approach plates and chart products: defer entirely for MVP (text-only), or include a "describe this approach" exercise that uses pre-extracted approach metadata? Default: defer.
- Self-reported checkride pass rate vs. verified (temporary airman cert upload) — see [00-product/success-metrics.md](../00-product/success-metrics.md).
