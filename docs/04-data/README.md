# 04 — Data ⭐ THE FIRST SLICE

Knowledge base and ingestion. **This is what we build first.** Until this works, every other layer is theoretical.

## Files

| File | Purpose | Status | Priority |
|---|---|---|---|
| `source-documents.md` | Tier-1 IR docs, where to download, license status, version pinning | stub | **P0** |
| `ingestion-pipeline.md` | PDF → chunks → embeddings → indexed, step by step | stub | **P0** |
| `chunking-strategy.md` | Specific rules: how to split ACS, regs, handbooks | stub | **P0** |
| `metadata-schema.md` | Exact schema every chunk must carry | stub | **P0** |
| `embedding-strategy.md` | Model choice, dimensions, hybrid search setup | stub | **P0** |
| `versioning.md` | What happens when FAA updates a doc | stub | P2 |

## Build order

1. `source-documents.md` — pin the Tier-1 list and confirm public-domain status before anything else.
2. `metadata-schema.md` — lock the chunk schema next; everything downstream depends on it.
3. `chunking-strategy.md` + `embedding-strategy.md` — these inform the pipeline.
4. `ingestion-pipeline.md` — the assembly. Once written, hand to Claude Code to implement.
5. `versioning.md` — fill once the first ingestion is working and we hit the first FAA update.

## Why this is P0

- Bad chunks → bad retrieval → bad generation → no amount of frontend polish saves the demo.
- This slice also produces the **eval set** ([08-testing/eval-sets.md](../08-testing/eval-sets.md)): once we can retrieve, we can ask "is the right chunk in the top-5?"

## Sources

[`../faa-acs-study-app-spec-v0.1.md`](../faa-acs-study-app-spec-v0.1.md) §4 (tighter) and [`../faa_acs_ai_study_app_spec_v0_1.md`](../faa_acs_ai_study_app_spec_v0_1.md) §4 (more exhaustive).
