# 06 — Infrastructure

Where it runs, how it gets there, what it costs.

## Files

| File | Purpose | Status | Priority |
|---|---|---|---|
| `environments.md` | local / staging / prod — what differs across them | stub | P1 |
| `hosting.md` | Vercel (frontend) + Render or Fly.io (backend) + managed Postgres + S3, with rationale | stub | P1 |
| `secrets.md` | API keys, env vars, what goes where, rotation policy | stub | P1 |
| `ci-cd.md` | GitHub Actions, deploy pipeline, eval gate | stub | P2 |
| `cost-model.md` | Per-user cost projection, levers to pull | stub | P1 |

## Why P1, not P0

The first slice (ingestion) runs locally. Production hosting only matters when we have a thing worth deploying.
