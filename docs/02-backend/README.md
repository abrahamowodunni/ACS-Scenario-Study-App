# 02 — Backend

Python/FastAPI server: API surface, services, data models, auth, errors.

See [01-architecture/tech-stack.md](../01-architecture/tech-stack.md) for the locked stack.

## Files

| File | Purpose | Status | Priority |
|---|---|---|---|
| `api-spec.md` | Every endpoint: method, path, request, response, errors | stub | **P0** for slice |
| `services.md` | Service layer — `QuestionService`, `GradingService`, `MasteryService`, `IngestionService` | stub | **P0** for slice |
| `data-models.md` | DB schema: users, sessions, questions, attempts, mastery, source docs, chunks | stub | **P0** |
| `auth.md` | Clerk integration, JWT verification, session handling | stub | P1 |
| `error-handling.md` | Error taxonomy + HTTP response format | stub | P1 |

## Conventions (to be formalized in `api-spec.md`)

- **Routing:** versioned under `/api/v1/`
- **Auth:** Bearer JWT (Clerk-issued); FastAPI dependency for verification
- **Errors:** RFC 7807 problem-details JSON
- **Validation:** Pydantic models for every request and response

## Sources

Initial data model sketches: [`../faa_acs_ai_study_app_spec_v0_1.md`](../faa_acs_ai_study_app_spec_v0_1.md) Appendix B.
