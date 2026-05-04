# 01 — Architecture

How the system fits together. Read this folder first if you're new to the codebase.

## Files

| File | Purpose | Status | Priority |
|---|---|---|---|
| `system-overview.md` | One-page diagram + narrative of all moving parts | stub | **P0** |
| `data-flow.md` | User query → retrieval → generation → response, in detail | stub | **P0** |
| `tech-stack.md` | Locked stack choices with rationale | **locked** | **P0** |
| `non-functional-requirements.md` | Latency, cost, accuracy targets | stub | P1 |

## When to update

- New external dependency (vector DB swap, LLM provider change) → update `tech-stack.md` and add an ADR in [09-decisions/](../09-decisions/)
- New service or data path → update `system-overview.md` + `data-flow.md`
- Performance target change → update `non-functional-requirements.md`
