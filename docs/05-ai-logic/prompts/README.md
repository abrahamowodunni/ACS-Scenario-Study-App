# Prompts

One file per prompt. Each file is the canonical version of that prompt — code references this, not an inline string.

## Files

| File | Purpose | Status | Priority |
|---|---|---|---|
| `question-generation.md` | System prompt + question-type variants (knowledge / scenario / risk / regulatory) | stub | **P0** |
| `free-response-grading.md` | Grading rubric prompt (Haiku-tier) | stub | P1 |
| `query-analyzer.md` | Cheap LLM that extracts ACS task + question type from user request | stub | **P0** |
| `validator.md` | LLM-as-judge that checks citations resolve and claims are supported | stub | **P0** |

## Prompt file template

Each prompt file should contain:

1. **Purpose** — what this prompt does in the pipeline
2. **Model** — which Claude tier (Sonnet for generation, Haiku for cheap ops)
3. **Inputs** — variables interpolated into the prompt
4. **Output schema** — strict JSON shape expected back
5. **Full prompt text** — verbatim
6. **Failure modes** — what to do when the model returns malformed output, refuses, or returns `insufficient_context`
7. **Eval notes** — which gold-set items exercise this prompt
8. **Changelog** — date + what changed + eval delta

## Why version-controlled here, not just in code

When (not if) we change a prompt, we need to know what changed and what the eval impact was. Inline strings make this nearly impossible.
