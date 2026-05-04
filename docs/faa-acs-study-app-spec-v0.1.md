# FAA ACS Study App — Product & Technical Specification

**Version:** 0.1 (initial draft)
**Status:** Living document — sections are independently editable
**Owner:** _[TODO: assign]_
**Last updated:** 2026-05-03

---

## How to use this document

Each numbered section is self-contained. Edit one without breaking the others. **DECISION** markers flag choices that need your input before we lock the design. **TODO** markers flag research tasks. **OPEN QUESTION** markers flag ambiguities surfaced from the original brief.

---

## 1. Product Vision & Problem Statement

### 1.1 Refined problem statement

Aspiring pilots preparing for FAA practical exams (checkrides) face a fragmented prep landscape. Existing tools fall into three buckets, each with gaps:

- **Question banks** (Sheppard Air, Sporty's written test prep) — drill the FAA *written* knowledge test using historical/leaked question pools. They train pattern-matching, not understanding, and don't cover the *oral* portion of the checkride well.
- **Video courses** (King Schools, Sporty's, Gold Seal) — strong for initial learning, weak for active recall and personalized weak-spot drilling.
- **Generic AI chatbots** — flexible and conversational, but hallucinate regulations, invent FAR citations, and aren't grounded in the ACS structure that examiners actually use.

The gap: there is no tool that generates **fresh, ACS-aligned, scenario-based practice questions grounded in authoritative FAA source material**, with explanations that cite the source, adapt to the user's weak areas, and prepare the candidate for the *oral exam* style of questioning a DPE actually uses.

### 1.2 Target audience personas

| Persona | Goal | Primary pain point | Willingness to pay |
|---|---|---|---|
| **Penny — Private Pilot candidate** | Pass PPL checkride in 3–6 months | Doesn't know what a DPE will ask in the oral; written test prep doesn't help | Moderate ($20–40/mo) |
| **Ian — Instrument Rating candidate** | Add IR after PPL | IR oral is dense (regs, approach plates, weather); needs scenario practice | Moderate–high |
| **Carlos — CFI candidate** | Pass CFI initial | Must teach, not just know; needs to articulate concepts, not just recall | High ($50+/mo, professional investment) |
| **Rita — Recurrent / flight review pilot** | Stay sharp, BFR prep | Casual; price-sensitive | Low |

**OPEN QUESTION:** Which persona is the v1 wedge? Recommendation below assumes **Instrument Rating candidates** — highest pain, dense regulatory material that benefits most from RAG, and a paying audience already used to spending on training. Confirm or redirect.

### 1.3 Value proposition & differentiation

> "Practice the oral exam your DPE will actually give you — generated fresh from the FAA's own materials, tuned to the ACS task you're weakest on."

Differentiation matrix:

| | Sheppard Air | Sporty's | King Schools | Generic ChatGPT | **This app** |
|---|---|---|---|---|---|
| Written test rote drill | ✅ | ✅ | ➖ | ➖ | ➖ (not the focus) |
| Oral / scenario prep | ❌ | ➖ | ➖ | ⚠️ hallucinates | ✅ |
| ACS-task-aligned | ❌ | ➖ | ➖ | ❌ | ✅ |
| Cited to FAA source | ❌ | ❌ | ❌ | ❌ | ✅ |
| Adaptive / weak-area focus | ❌ | ➖ | ❌ | ❌ | ✅ |
| Fresh questions (not memorized pool) | ❌ | ❌ | n/a | ✅ | ✅ |

### 1.4 Success metrics

**Leading indicators (product health):**
- Question accuracy rate (graded by SME audit) — target ≥95% factually correct, ≥90% ACS-aligned
- Citation correctness — target 100% of cited FAR/AIM references resolve to the actual source
- Session length and weekly retention (W1, W4)
- Hallucination rate per 1,000 generated questions — target <1%

**Lagging indicators (outcomes):**
- Self-reported checkride pass rate vs. national average (FAA publishes this; PPL ~80%, IR ~80%)
- NPS from users who completed their checkride
- Conversion: free trial → paid

**DECISION:** Are we comfortable measuring pass rate via self-report initially, or do we want a verification step (upload temporary airman certificate)? Self-report is faster but noisy.

---

## 2. Functional Requirements

### 2.1 Core features (MVP)

1. **ACS-aligned question generation** — user picks a certificate (PPL/IR/Commercial/CFI) and an Area of Operation / Task; system generates a question grounded in the relevant FAA source chunks.
2. **Question types:**
   - Knowledge recall (definitions, limits, regs)
   - Scenario-based ("You're 20nm from your destination at 8,000 ft and notice…")
   - Risk management (PAVE, IMSAFE, 5P applied to a scenario)
   - Regulatory interpretation ("Under what conditions can you…")
3. **Free-response grading** — user types or speaks their answer; LLM grades against the ACS knowledge/risk/skill element and the cited source, returns a rubric-style score and explanation.
4. **Source citations** — every question and every grade explanation links to the FAA document, section, and page.
5. **Progress tracking** — per-ACS-task mastery score, weak-area heat map.
6. **Adaptive next-question selection** — bias toward weak areas, with spaced repetition.

### 2.2 User flows

**Sign-up → first session (target: <3 min to first question):**
1. Email/OAuth sign-up
2. Pick certificate target (PPL, IR, etc.) and target checkride date
3. Optional: 10-question diagnostic to seed the mastery model
4. Land on dashboard → "Start Study Session"

**Study session loop:**
1. System picks ACS task (weighted by weakness + spacing)
2. Generates question with retrieved context
3. User answers (free response or multiple-choice toggle)
4. LLM grades + explains + cites
5. User rates question quality (👍/👎 — feeds eval set)
6. Mastery model updates → next question

**Performance review (weekly digest):**
- Mastery heat map across ACS areas
- Top 3 weak tasks with recommended reading
- Predicted readiness percentage

### 2.3 Content scope by phase

| Phase | Certificates | ACS Areas covered |
|---|---|---|
| **MVP** | Instrument Rating only | All 7 IR areas of operation |
| **Phase 2** | + Private Pilot Airplane | All PPL areas |
| **Phase 3** | + Commercial, CFI | Full coverage |

**OPEN QUESTION:** Original brief said "FAA ACS examination" generally. Confirm IR-first wedge, or pick a different starting cert.

---

## 3. Technical Architecture Proposal

### 3.1 Recommended approach: **RAG with metadata-filtered retrieval**

**Why RAG wins for this domain:**
- FAA materials are large (thousands of pages), authoritative, and updated regularly. Fine-tuning on them locks the model to a snapshot and is expensive to refresh.
- Citation requirement is non-negotiable — RAG naturally produces grounded references; fine-tuning does not.
- ACS structure (Area → Task → Element) is metadata-rich and maps cleanly to vector DB filtering.
- Hallucination risk is the single biggest product threat; RAG with strict "answer only from context" prompting is the strongest mitigation available without custom training.

### 3.2 Alternatives evaluated

| Approach | Pros | Cons | Verdict |
|---|---|---|---|
| **Pure prompt-stuffing** (paste FAA docs into context) | Simple; no infra | Context window limits; expensive per call; can't scale to full FAA corpus; poor task-specific retrieval | ❌ Doesn't scale |
| **Fine-tuning** on FAA corpus | Fast inference; no retrieval latency | Expensive to retrain on FAA updates; no citations; baked-in hallucination risk; locks vendor | ❌ Wrong tool |
| **RAG (vector + LLM)** ← recommended | Citations, updatable corpus, metadata filtering, vendor-flexible | Retrieval quality is the bottleneck; chunking strategy matters | ✅ Default |
| **Hybrid: RAG + light fine-tune** for tone/format | Combines grounded retrieval with consistent question format | Complexity, cost, only worth it after MVP eval data exists | 🟡 Phase 2+ |
| **Agentic retrieval** (LLM iteratively searches) | Better for complex multi-hop questions ("compare IFR vs VFR fuel reserves") | Higher latency, higher cost, harder to evaluate | 🟡 Phase 2 for complex scenarios |

### 3.3 Recommended tech stack

| Layer | Recommendation | Rationale | Alternatives |
|---|---|---|---|
| **LLM** | Claude (Sonnet for generation, Haiku for grading/cheap ops) | Strong instruction-following, citation behavior, long context | GPT-4-class, open-source (Llama 3.1 70B) for cost control later |
| **Embeddings** | `voyage-3` or OpenAI `text-embedding-3-large` | Strong on technical/regulatory text | Cohere embed-v3, BGE-large (self-hosted) |
| **Vector DB** | **pgvector on Postgres** (MVP) → Pinecone or Weaviate (scale) | pgvector keeps everything in one DB, simplifies metadata joins, free; migrate when scale demands | Chroma (dev), Pinecone (managed), Weaviate (hybrid search built-in) |
| **Backend** | Node/TypeScript (Next.js API routes or Fastify) **or** Python (FastAPI) | TS if frontend-heavy and solo dev; Python if heavy ML/eval tooling | — |
| **Frontend** | Next.js + Tailwind + shadcn/ui | Fast to build, good DX, easy auth | Remix, SvelteKit |
| **Auth/billing** | Clerk + Stripe | Skip the undifferentiated work | Auth.js, Supabase Auth |
| **Eval harness** | Custom + Braintrust or Langfuse | Need this from day one to track hallucination rate | Promptfoo, Ragas |

**DECISION:** Backend language — TypeScript (one stack) or Python (better ML ecosystem)? Default recommendation: **TypeScript** for solo dev velocity unless you're already Python-fluent.

### 3.4 Data flow

```
User query
    │
    ▼
[1] Query analyzer (LLM, cheap model)
    │  → extracts: certificate, ACS area code, task code, question type
    ▼
[2] Retrieval
    │  → vector search over chunks
    │  → metadata filter: certificate=IR, area=II, etc.
    │  → top-k=5–8 chunks
    ▼
[3] Reranker (optional, Phase 2)
    │  → cross-encoder rerank to top-3
    ▼
[4] Context assembly
    │  → chunks + ACS task definition + question-type template
    ▼
[5] LLM generation (Claude Sonnet)
    │  → grounded question + answer + citation
    ▼
[6] Validator (LLM-as-judge, Haiku)
    │  → checks citation resolves, claim is in context
    │  → if fail: regenerate (max 1 retry)
    ▼
Response to user
```

### 3.5 Cost / latency / accuracy tradeoffs

Rough per-question economics at MVP scale (assumes Claude pricing as of 2026, verify before launch):

| Choice | Cost/question | Latency | Accuracy impact |
|---|---|---|---|
| Sonnet generation only | ~$0.01–0.02 | ~3–5s | Baseline |
| + Validator pass (Haiku) | +~$0.002 | +~1s | -50–70% hallucination |
| + Reranker | +~$0.001 | +~0.5s | +retrieval precision |
| Agentic multi-hop | 3–5× | 10–20s | Best for complex scenarios |

**TODO:** Pull current Claude pricing and rebuild this table before committing to unit economics.

---

## 4. Knowledge Base & Data Ingestion

### 4.1 Authoritative source documents

**Tier 1 — must ingest for MVP:**
- FAA-S-ACS-8B (Instrument Rating ACS) — *the* structural backbone
- FAA-H-8083-15B Instrument Flying Handbook
- FAA-H-8083-25C Pilot's Handbook of Aeronautical Knowledge (PHAK)
- FAA-H-8083-16B Instrument Procedures Handbook
- 14 CFR Part 61 (certification)
- 14 CFR Part 91 (general operating rules)
- AIM (Aeronautical Information Manual)

**Tier 2 — Phase 2:**
- FAA-S-ACS-6B (Private Pilot Airplane ACS)
- FAA-H-8083-3C Airplane Flying Handbook
- Relevant Advisory Circulars (AC 00-6B Aviation Weather, AC 00-45H Aviation Weather Services, AC 90-100A RNAV, etc.)
- 14 CFR Part 71, 97
- Airport/Facility Directory style data (Chart Supplement)

### 4.2 Preprocessing pipeline

```
PDF → text extraction → structural parse → chunking → metadata enrichment → embedding → index
```

1. **Extraction:** `pdfplumber` or `pypdf` for text-heavy docs; `unstructured.io` for mixed layout. Manual QA on table-heavy sections (weight & balance, performance charts).
2. **Structural parse:** preserve hierarchy (Chapter → Section → Subsection). For ACS, parse the Area/Task/Element tree explicitly — this metadata is gold.
3. **Chunking strategy:**
   - Default: **semantic chunking** (~500–800 tokens) with 100-token overlap
   - For regulations: **regulation-section-as-chunk** (don't split §91.103)
   - For ACS: **task-element-as-chunk** (each knowledge/risk/skill element is a unit)
4. **Metadata schema** (every chunk gets these):
   ```json
   {
     "doc_id": "FAA-S-ACS-8B",
     "doc_title": "Instrument Rating ACS",
     "doc_version": "2024-05",
     "section": "Area II, Task A",
     "page": 14,
     "acs_area_code": "II",
     "acs_task_code": "II.A",
     "acs_element_type": "knowledge | risk | skill | null",
     "certificate": "IR",
     "regulatory_ref": "14 CFR 91.167",
     "source_url": "https://..."
   }
   ```

### 4.3 Embedding strategy

- Embed full chunk text + a synthetic "summary line" prepended (improves retrieval on dense regulatory text)
- Store both dense embeddings and a BM25/keyword index for **hybrid search** — regulations have specific terms ("§91.175(c)") that lexical search nails and embeddings sometimes miss
- Re-embed when changing models; version the embedding model in metadata

### 4.4 Update & version control

- FAA publications change on a schedule (ACS revisions, CFR amendments, AIM cycle ~every 6 months)
- Pipeline must be **rerunnable**: source docs in S3 (or equivalent) by version, ingestion is idempotent
- Each chunk carries `doc_version`; queries can filter to "current" or specific version
- **Diff alerts:** when a new FAA doc version drops, automated diff highlights changed sections for SME review before going live
- **TODO:** Subscribe to FAA Federal Register notifications and AIM change notices for change detection

---

## 5. Prompt Engineering Strategy

### 5.1 System prompt template (question generation)

```
You are an expert FAA flight instructor and Designated Pilot Examiner generating
practice questions for a {{certificate}} candidate preparing for their checkride.

You will be given:
- An ACS Area of Operation and Task
- Authoritative source excerpts from FAA publications
- A question type to generate

CRITICAL RULES:
1. Generate questions ONLY from facts present in the provided source excerpts.
2. If the excerpts do not support a claim, do NOT make the claim.
3. Every factual claim in the answer must cite the source document and section.
4. Match the cognitive level the ACS task specifies (recall vs. understand vs. apply).
5. Do not reproduce verbatim text from the source — rephrase as a question.
6. If you cannot generate a sound question from the provided context, respond
   with {"error": "insufficient_context"} and stop.

Output JSON:
{
  "question": "...",
  "question_type": "knowledge|scenario|risk|regulatory",
  "expected_answer": "...",
  "rubric": ["key point 1", "key point 2", ...],
  "citations": [{"doc": "...", "section": "...", "page": N}],
  "acs_element": "II.A.K3"
}
```

### 5.2 Question-type sub-templates

**Knowledge recall:**
> "Generate a direct question testing the candidate's recall of the concept defined in the source. Avoid trick wording."

**Scenario-based:**
> "Construct a realistic flight scenario where the candidate must apply the concept. Include: aircraft state, location/route, weather, and the decision point. End with an open question."

**Risk management:**
> "Construct a scenario where multiple risk factors are present. Ask the candidate to identify hazards and apply [PAVE | IMSAFE | 5P | DECIDE]."

**Regulatory interpretation:**
> "Pose a situation that hinges on a specific regulatory threshold. The candidate must cite the rule and apply it. Source must include the actual CFR text."

### 5.3 Hallucination guardrails

- **Context-only prompting** (rule 1 above) — primary defense
- **Validator pass:** second LLM call checks each citation resolves to a real chunk ID and that the claim text is supported by that chunk
- **Citation roundtrip:** the citation field must reference a `chunk_id` returned by retrieval — anything else is rejected
- **Refusal path:** the model is instructed to return `insufficient_context` rather than guess; we'd rather show "no question available for this task yet" than a wrong question
- **Eval set:** 200+ SME-graded questions baselined; CI runs the eval on every prompt change

### 5.4 Free-response grading prompt

```
You are grading a checkride candidate's free-response answer.

ACS task: {{task}}
ACS element: {{element}}
Rubric (key points the answer should hit): {{rubric}}
Source excerpts: {{context}}
Candidate answer: {{answer}}

For each rubric point: HIT / PARTIAL / MISS, with one-sentence justification grounded in the source.
Then: overall verdict (Satisfactory / Unsatisfactory per ACS standards) and a constructive next step.

If the candidate's answer contradicts the source, point to the source explicitly.
Do not invent rubric points not in the list.
```

### 5.5 Few-shot example (abbreviated)

**Input context:** chunk from 14 CFR 91.167 (IFR fuel requirements) + ACS task II.A "Pilot Qualifications"

**Desired output:**
```json
{
  "question": "You're planning an IFR flight from KPHX to KABQ, ETA 14:30Z. Forecast at KABQ at ETA is 800 overcast, 2 SM visibility in light snow. Are you required to file an alternate? If so, what fuel reserve must you carry?",
  "question_type": "regulatory",
  "expected_answer": "Yes, alternate required because forecast is below 2,000 ft / 3 SM at ETA ±1 hour (the 1-2-3 rule). Fuel reserve: enough to fly to destination, then to alternate, then 45 minutes at normal cruise.",
  "rubric": ["Identifies 1-2-3 rule applies", "Concludes alternate required", "States fuel = dest + alt + 45 min"],
  "citations": [{"doc": "14 CFR 91.167", "section": "(a),(b)", "page": null}],
  "acs_element": "II.A.K1"
}
```

---

## 6. Development Roadmap

### Phase 1 — MVP (target: 10–14 weeks solo, faster with help)

**Scope:** Instrument Rating only. Tier-1 docs ingested. Web app, single user flow.

Must-have:
- Auth, billing skeleton (free trial)
- Ingestion pipeline + initial corpus indexed
- Question generation for all 4 types
- Free-response grading
- Per-task mastery tracking + adaptive selection
- Citations on every question and grade
- Internal eval harness running ≥200 SME-graded items

Out of scope: mobile, voice, instructor mode, community.

### Phase 2 — Depth (target: +8–12 weeks)

- Add PPL Airplane content
- Reranker, hybrid search
- Spaced repetition tuning based on real usage data
- Weekly digest emails
- Light fine-tune for question style consistency (decide based on Phase 1 eval data)

### Phase 3 — Reach (target: +12+ weeks)

- Mobile (React Native or PWA-first)
- Voice answer mode (oral exam realism)
- Instructor / CFI mode — assign tasks to students, view their progress
- Community: shared scenarios, leaderboards (carefully, to avoid teaching-to-the-test)
- Commercial, CFI, ATP content

### 6.1 Decisions deferred

- Native mobile vs. PWA — wait for Phase 1 usage data
- Self-hosted open-source LLM — only if unit economics demand
- Marketplace for instructor-authored scenario packs

---

## 7. Risks & Open Questions

### 7.1 Legal & copyright

- FAA publications produced by the U.S. government are **generally public domain** under 17 USC §105, but verify each source — some incorporate third-party content (e.g., Jeppesen charts, ICAO material) that is **not** public domain.
- **TODO:** Legal review of every Tier-1 document before launch. Specifically check: AIM (yes, government work), advisory circulars (yes), any chart products (Jeppesen no, FAA sectionals yes), test prep materials from third parties (no — do not ingest).
- Trademark: "ACS" and FAA branding — don't imply endorsement. "FAA ACS-aligned, not FAA-affiliated" disclaimer.

### 7.2 Hallucination risk

Already addressed at the architecture/prompt level (§3, §5). Residual risks:
- Source itself is ambiguous (regs sometimes are) — model may pick a defensible-but-wrong interpretation. Mitigation: SME review of generated questions in weak ACS areas.
- Edge-case ACS tasks with thin source coverage. Mitigation: explicit `insufficient_context` refusal, manual question authoring fallback for thin tasks.

### 7.3 Cost projections (rough, MVP scale)

Assumptions: 1,000 active users, 50 questions/user/week, validator pass on each:

- ~200K questions/week × ~$0.015/question all-in = **~$3K/week LLM cost** at scale
- Vector DB (pgvector on managed Postgres): ~$50–200/mo at MVP scale
- Hosting (Vercel/Render): ~$50–200/mo
- **TODO:** Rebuild with current pricing; identify Haiku-tier opportunities to cut generation cost

### 7.4 Items needing further research

- Confirm IR-first wedge vs. PPL-first (§1.2, §2.3)
- Self-report vs. verified pass-rate metric (§1.4)
- Backend language choice (§3.3)
- Whether to build voice answer mode in Phase 2 vs. Phase 3 — DPEs grade on verbal articulation, so this may be more central than "Phase 3" suggests
- Pricing model: flat monthly, per-certificate one-time, or freemium with paid weak-area drilling
- SME network: who reviews the eval set? Recruit 2–3 active CFIIs on retainer

---

## Appendix A — Glossary

- **ACS** — Airman Certification Standards. The FAA document defining what a candidate must know/do/manage for a given certificate.
- **Area of Operation** — top-level grouping in the ACS (e.g., "Preflight Preparation").
- **Task** — subdivision of an Area (e.g., "Pilot Qualifications").
- **Element** — atomic knowledge/risk/skill item within a Task.
- **DPE** — Designated Pilot Examiner. Conducts checkrides on the FAA's behalf.
- **RAG** — Retrieval-Augmented Generation.
- **Hybrid search** — combining dense (vector) and sparse (keyword/BM25) retrieval.

---

## Appendix B — Change log

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-05-03 | Initial draft |

---

_End of v0.1. Send specific section feedback (e.g., "redo §3.3 assuming Python backend" or "tighten §1.2 around CFI persona") rather than asking for a full regenerate — this doc is designed for surgical edits._
