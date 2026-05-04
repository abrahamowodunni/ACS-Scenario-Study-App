# FAA ACS AI Study App — Product & Technical Architecture Spec

**Version:** v0.1  
**Status:** First Draft  
**Audience:** Technical founder, solo developer, product collaborator, or early engineering/design partner  
**Product Domain:** Aviation education technology  
**Primary Users:** Student pilots and aviation candidates preparing for FAA Airman Certification Standards examinations  

---

## Document Purpose

This document defines the first structured product and technical architecture proposal for an AI-powered FAA ACS study application. It is intended to be a living, version-controllable product specification that can be refined over time as the product, user base, data pipeline, and technical implementation mature.

The core recommendation is to build the application around a **Retrieval-Augmented Generation (RAG)** architecture. RAG is recommended because the product’s value depends on generating accurate, FAA-grounded study questions, explanations, and adaptive guidance from authoritative aviation materials rather than relying on unsupported model memory.

---

# 1. Product Vision & Problem Statement

## 1.1 Refined Problem Statement

Aspiring pilots preparing for FAA ACS-based examinations often rely on static question banks, video courses, flashcards, or generic AI chatbots. These tools can be helpful, but they create several gaps:

- **Static memorization instead of understanding:** Many learners memorize known question banks without developing the deeper reasoning needed for oral exams, checkrides, scenario-based evaluation, and real-world aeronautical decision-making.
- **Limited personalization:** Traditional study tools may not adapt deeply to a learner’s weak areas, recurring mistakes, risk-management blind spots, or preferred learning style.
- **Generic AI hallucination risk:** General-purpose AI tools can produce confident but incorrect aviation explanations, cite nonexistent sources, or generate questions that are not aligned with FAA ACS standards.
- **Fragmented source material:** FAA materials are authoritative but spread across multiple long documents, including ACS publications, FAA handbooks, the AIM, and regulations.
- **Poor traceability:** Learners often cannot easily see exactly which FAA source supports a study explanation or practice question.

The product should solve this by providing an interactive, personalized study environment that generates FAA-aligned practice questions, scenario prompts, explanations, and study guidance grounded in curated official source material.

## 1.2 Product Vision

Build a web-based AI study application that helps aviation candidates prepare for FAA ACS exams by combining:

- Official FAA source documents
- Retrieval-Augmented Generation
- Scenario-based question generation
- Personalized weak-area tracking
- Source-grounded explanations
- Adaptive study recommendations

The long-term vision is not merely to create another question bank, but to create a **grounded aviation learning engine** that teaches users how to reason like safe, competent pilots.

## 1.3 Target Audience Personas

### Persona 1: Private Pilot Candidate

**Profile:** A student pilot preparing for the Private Pilot Airplane ACS and checkride.  
**Pain Points:**

- Struggles to connect written exam knowledge with oral/checkride scenarios
- Needs help understanding weather, airspace, performance, navigation, and regulations
- Wants practice questions that explain why an answer is correct

**Product Value:**

- Generates ACS-aligned knowledge and scenario questions
- Provides explanations tied to FAA sources
- Tracks weak ACS tasks over time

### Persona 2: Instrument Rating Candidate

**Profile:** A pilot preparing for the Instrument Rating ACS.  
**Pain Points:**

- Needs scenario-heavy IFR practice
- Must understand regulations, procedures, weather products, approach charts, and risk management
- Needs practice applying concepts under realistic decision-making constraints

**Product Value:**

- Produces IFR scenario-based questions
- Helps identify weak regulatory and procedural areas
- Supports structured study by ACS area/task

### Persona 3: CFI Candidate

**Profile:** A commercial pilot preparing to become a Certified Flight Instructor.  
**Pain Points:**

- Needs to explain concepts clearly, not just answer questions
- Must prepare lesson plans and demonstrate instructional knowledge
- Needs practice teaching from FAA-approved concepts

**Product Value:**

- Generates teaching-oriented prompts
- Provides explanations and source references
- Supports “teach this concept back” free-response evaluation

### Persona 4: Returning Pilot / Rusty Pilot

**Profile:** A certificated pilot refreshing knowledge after time away from flying.  
**Pain Points:**

- Needs targeted review, not a full course from scratch
- May be weak on updated regulations, airspace, weather products, or procedures

**Product Value:**

- Diagnostic assessment identifies knowledge gaps
- Adaptive review focuses on weak areas
- Source-grounded answers reduce misinformation risk

## 1.4 Value Proposition

The application helps pilots study smarter by generating personalized, FAA-grounded, ACS-aligned practice questions and explanations from official source material.

A concise positioning statement:

> An AI-powered FAA ACS study assistant that creates personalized, source-grounded practice questions, explanations, and scenario training from official FAA materials.

## 1.5 Differentiation From Existing Tools

Existing aviation study tools such as Sporty’s, King Schools, and Sheppard Air are well-known and valuable, but they tend to be course-driven, video-driven, or fixed-question-bank-driven.

This product can differentiate through:

- **Dynamic question generation:** New questions can be generated from source material instead of relying only on a fixed bank.
- **Scenario-based reasoning:** The app can produce oral exam/checkride-style prompts, not just multiple-choice recall.
- **Source traceability:** Every generated explanation should cite the FAA source material used.
- **Personalized weak-area remediation:** The system can track performance by ACS area, task, knowledge element, risk element, and skill element.
- **Interactive tutoring:** Learners can ask follow-up questions and receive grounded explanations.
- **Version-aware content:** FAA document updates can be tracked, re-ingested, and associated with specific app versions.

## 1.6 Success Metrics

### Learning Outcomes

- User pass rates for written exams and checkrides
- Improvement in diagnostic scores over time
- Reduction in repeated weak-area errors
- Performance improvement by ACS area/task

### Product Quality

- Question accuracy rate based on expert review
- Percentage of generated questions with valid source citations
- Hallucination or unsupported-claim rate
- User-reported explanation usefulness

### Engagement

- Weekly active users
- Study sessions per user per week
- Average session duration
- Question completion rate
- Return rate after first diagnostic assessment

### Business Metrics

- Free-to-paid conversion rate
- Subscription retention
- Cost per generated study session
- Customer acquisition cost
- Instructor/referral adoption rate

---

# 2. Functional Requirements

## 2.1 Core Features

### 2.1.1 Account Creation & User Profile

Users should be able to:

- Create an account
- Select certificate/rating goal
- Choose target exam/checkride date
- Identify experience level
- Select preferred study mode

Potential study goals:

- Private Pilot Airplane
- Instrument Rating Airplane
- Commercial Pilot Airplane
- CFI Airplane
- Future: Remote Pilot, Multi-Engine, ATP

### 2.1.2 Diagnostic Assessment

The app should generate or present a baseline assessment mapped to ACS categories.

Diagnostic output should include:

- Overall readiness score
- Weak ACS areas
- Weak task codes
- Knowledge gaps
- Risk-management gaps
- Recommended study plan

### 2.1.3 Question Generation

The system should generate FAA-grounded questions in several formats:

- Multiple-choice questions
- Short-answer questions
- Scenario-based questions
- Oral exam style prompts
- Risk-management decision questions
- Regulatory interpretation questions

Each generated question should include:

- Question text
- Correct answer or grading rubric
- Explanation
- Source citation/reference
- ACS mapping metadata
- Difficulty level
- Concept tags

### 2.1.4 Scenario-Based Study Mode

The app should support realistic aviation scenarios such as:

- Cross-country flight planning
- Weather go/no-go decision
- Airspace transition
- Fuel planning
- Performance limitations
- Instrument approach decision-making
- Diversion planning
- Emergency decision-making

Each scenario should test both knowledge and judgment.

### 2.1.5 Explanation Engine

After answering, users should receive:

- Correct/incorrect feedback
- FAA-grounded explanation
- Why other answer choices are wrong
- Related ACS task references
- Suggested follow-up study

### 2.1.6 Progress Tracking

The app should track:

- Questions answered
- Accuracy over time
- Confidence level
- Repeated mistakes
- Weak ACS areas/tasks
- Improvement trend
- Time spent by topic

### 2.1.7 Weak-Area Identification

The app should identify weak areas using:

- Incorrect answers
- Low-confidence answers
- Slow response times
- Repeated misses in same ACS category
- Poor free-response quality
- Missed risk-management reasoning

### 2.1.8 Adaptive Study Guidance

The app should recommend:

- Next study session topic
- Concepts to review
- FAA source sections to read
- Practice question types
- Scenario drills
- Review intervals based on spaced repetition

### 2.1.9 Free-Response Evaluation

Users should be able to answer open-ended questions. The system should evaluate:

- Accuracy
- Completeness
- Source alignment
- Risk-management reasoning
- Clarity of explanation
- Missing concepts

The system should avoid grading as if there is only one exact phrasing. It should compare against a rubric generated from retrieved FAA context.

## 2.2 User Flow

### Flow 1: First-Time User Onboarding

1. User signs up.
2. User selects certificate/rating goal.
3. User enters target exam/checkride date.
4. User selects current experience level.
5. User completes diagnostic assessment.
6. App generates readiness report.
7. App recommends a study path.

### Flow 2: Standard Study Session

1. User selects “Start Study Session.”
2. App chooses weak-area topic or user-selected ACS area.
3. RAG system retrieves relevant FAA source chunks.
4. LLM generates practice questions.
5. User answers questions.
6. App provides explanations and citations.
7. App updates performance profile.
8. App recommends next review.

### Flow 3: Scenario Practice

1. User selects scenario mode.
2. User chooses topic or difficulty.
3. App generates realistic flight scenario.
4. User responds to decisions/questions.
5. App grades reasoning using retrieved FAA source context.
6. App identifies gaps and suggests review.

### Flow 4: Performance Review

1. User opens dashboard.
2. App displays readiness by ACS area/task.
3. User reviews weak areas.
4. User selects a recommended drill.
5. App tracks improvement over time.

## 2.3 Initial Content Scope

### MVP Content Scope

Recommended MVP should focus on one high-demand certification path first:

**Recommended initial focus:** Private Pilot Airplane ACS

Initial areas:

- Preflight Preparation
- Weather Information
- National Airspace System
- Performance and Limitations
- Operation of Systems
- Human Factors
- Risk Management
- Regulations

### Later Content Expansion

Phase 2 and beyond:

- Instrument Rating Airplane ACS
- Commercial Pilot Airplane ACS
- CFI ACS/PTS-related preparation
- Multi-engine airplane
- Remote Pilot
- Flight review / rusty pilot mode

## 2.4 Non-Functional Requirements

The application should be:

- Accurate and source-grounded
- Low-latency enough for interactive study
- Auditable for source traceability
- Modular in content ingestion
- Version-aware when FAA documents update
- Secure with user performance data
- Cost-controlled at scale
- Designed for expert review workflows

---

# 3. Technical Architecture Proposal

## 3.1 Recommended Architecture

The recommended architecture is **Retrieval-Augmented Generation (RAG)** using curated FAA source documents, vector search, metadata filtering, and an LLM generation layer.

### Why RAG Is the Recommended Path

RAG is the strongest default architecture because:

- The product must stay grounded in authoritative FAA sources.
- FAA materials change over time, making static model memory risky.
- Users need traceable explanations and citations.
- Fine-tuning alone does not guarantee factual grounding.
- Prompt-stuffing entire documents is inefficient, costly, and limited by context windows.
- Metadata-based retrieval can align questions with ACS areas, tasks, and knowledge/risk/skill elements.

## 3.2 High-Level Architecture

```text
User Request / Study Goal
        ↓
Application Backend
        ↓
ACS Metadata Filter + Retrieval Query Builder
        ↓
Vector Database / Hybrid Search
        ↓
Relevant FAA Source Chunks
        ↓
Prompt Assembly / Context Injection
        ↓
LLM Question or Explanation Generation
        ↓
Validation / Guardrails / Citation Check
        ↓
User Interface Response
        ↓
Performance Tracking + Analytics Store
```

## 3.3 Data Flow Description

### Example: Scenario Question Generation

1. User selects “Weather Decision-Making — Private Pilot.”
2. Backend maps this request to relevant ACS metadata.
3. Retrieval query is generated using topic, certificate level, difficulty, and weak-area history.
4. Vector database retrieves relevant chunks from FAA ACS, PHAK, AIM, and related sources.
5. Retrieved chunks are passed into a structured prompt.
6. LLM generates a question, answer, explanation, distractors, and source references.
7. Output validator checks that the answer is supported by retrieved context.
8. App displays the question to the user.
9. User answer is recorded and mapped back to ACS performance analytics.

## 3.4 Architecture Options Considered

## Option A: RAG Architecture

### Description

Use embeddings and retrieval to fetch relevant FAA source chunks at runtime, then pass those chunks into an LLM prompt for grounded generation.

### Pros

- Strong factual grounding
- Easier document updates
- Supports source citations
- Good fit for FAA document-heavy domain
- Allows ACS metadata filtering
- Avoids relying only on model memory

### Cons

- Requires ingestion pipeline
- Retrieval quality must be carefully tuned
- Chunking strategy matters
- More moving parts than a static prompt approach
- Citation validation requires additional logic

### Recommendation

Use as the core architecture.

---

## Option B: Fine-Tuning

### Description

Fine-tune a model on aviation question-answer pairs, explanations, or FAA-aligned examples.

### Pros

- Can improve style consistency
- Can teach desired output format
- Can reduce prompt length for repeated patterns
- Useful later for specialized grading or question formatting

### Cons

- Does not guarantee factual correctness
- Harder to update when FAA documents change
- Requires high-quality training data
- Can encode outdated information
- More expensive and operationally complex early on

### Recommendation

Do not use fine-tuning for MVP factual grounding. Consider later for style, grading consistency, or structured output behavior after collecting validated examples.

---

## Option C: Prompt-Stuffing

### Description

Insert large sections of FAA documents directly into the prompt without a retrieval system.

### Pros

- Simple prototype path
- No vector database required
- Useful for quick experiments with small document sections

### Cons

- Expensive at scale
- Latency increases with context size
- Context windows are still finite
- Hard to manage many documents
- Poor long-term architecture for a full ACS app

### Recommendation

Use only for prototypes or internal testing. Do not use as the production architecture.

---

## Option D: Hybrid Search + RAG

### Description

Combine vector similarity search with keyword/BM25 search and metadata filters.

### Pros

- Better retrieval accuracy for aviation terminology
- Handles exact regulatory references better
- Supports semantic and literal matching
- Useful for ACS task codes, FAR references, and FAA terminology

### Cons

- More complex retrieval infrastructure
- Requires scoring/ranking strategy
- Needs evaluation dataset

### Recommendation

Strongly recommended after MVP or even during MVP if implementation complexity is acceptable.

---

## Option E: Agentic Retrieval

### Description

Use an agent-like workflow where the model decides which sources to search, performs multiple retrieval steps, compares results, and then generates an answer.

### Pros

- Useful for complex multi-document questions
- Can improve deep reasoning workflows
- Good for advanced tutoring and research mode

### Cons

- Higher latency
- Higher cost
- More difficult to control
- More failure modes
- Harder to validate deterministically

### Recommendation

Do not use for the basic question generator in MVP. Consider later for advanced “ask an instructor” or deep explanation mode.

## 3.5 Recommended Tech Stack

## Frontend

### Recommended

- **Next.js / React**
- Tailwind CSS
- shadcn/ui or similar component system

### Reasoning

Next.js is a strong choice for a solo developer or small team because it supports fast UI development, routing, server components, API routes if needed, and deployment on platforms like Vercel.

## Backend

### Recommended

- **FastAPI** or **Node.js/NestJS**

### FastAPI Pros

- Excellent for AI/RAG workflows
- Strong Python ecosystem for PDF parsing, embeddings, and evaluation
- Easy integration with LangChain, LlamaIndex, Instructor, Pydantic, and vector DB clients

### Node/NestJS Pros

- Strong full-stack TypeScript consistency
- Good API structure for larger teams
- Works well if frontend/backend TypeScript unification matters

### Recommendation

Use **FastAPI** for MVP if the developer is AI/RAG-focused and wants faster experimentation with Python tooling.

## Vector Database

### Options

| Option | Pros | Cons | Recommendation |
|---|---|---|---|
| pgvector | Simple, Postgres-native, good for MVP, easy metadata | May need tuning at scale | Strong MVP choice |
| Pinecone | Managed, scalable, fast | Vendor cost, less control | Good if speed-to-market matters |
| Weaviate | Hybrid search, metadata, scalable | More infrastructure complexity | Strong if hybrid retrieval is priority |
| Chroma | Very easy local prototyping | Less ideal for production scale | Good for prototype only |
| Qdrant | Strong vector search, filtering, open source | Another service to manage | Strong production candidate |

### Recommendation

Use **pgvector** for MVP if simplicity and cost control matter. Use **Pinecone** or **Qdrant** if managed scale and retrieval performance become higher priorities.

## Embedding Model

### Options

- OpenAI text embedding models
- Cohere embeddings
- Voyage embeddings
- BGE / instructor-style open-source embeddings

### Recommendation

For MVP, use a high-quality hosted embedding model to reduce operational complexity. Later, benchmark against open-source embeddings for cost control.

Important evaluation criteria:

- Retrieval accuracy on aviation terminology
- Handling of regulatory references
- Cost per embedded document and query
- Latency
- Metadata compatibility

## LLM Provider

### Options

- OpenAI GPT models
- Anthropic Claude models
- Google Gemini models
- Open-source models hosted through Together, Fireworks, Groq, vLLM, or similar

### Recommendation

Use a strong general-purpose hosted LLM for MVP because accuracy and instruction-following matter more than infrastructure control early on.

Recommended model qualities:

- Strong reasoning
- Good structured JSON output
- Reliable instruction following
- Low hallucination tendencies
- Affordable enough for repeated study sessions

## Database

Use PostgreSQL for:

- Users
- Study sessions
- Question attempts
- Performance analytics
- ACS mappings
- Source document metadata
- Subscription/billing state

## Object Storage

Use S3-compatible storage for:

- Raw PDFs
- Parsed text files
- Chunked JSONL records
- Evaluation datasets
- Versioned source snapshots

## 3.6 Cost, Latency, and Accuracy Tradeoffs

### RAG Cost Factors

- Embedding documents during ingestion
- Embedding user queries
- Vector database storage/query cost
- LLM input tokens from retrieved context
- LLM output tokens for generated questions/explanations

### Latency Factors

- Query embedding latency
- Vector search latency
- Reranking latency if used
- LLM generation latency
- Validation pass latency

### Accuracy Factors

- Quality of source documents
- Chunking strategy
- Retrieval ranking
- Metadata filters
- Prompt clarity
- Output validation
- Expert-reviewed evaluation set

### MVP Tradeoff Recommendation

For MVP, prioritize:

1. Accuracy
2. Traceability
3. Simple architecture
4. Cost control
5. Latency

A study tool can tolerate slightly slower responses if the answers are trustworthy. It cannot tolerate fast but wrong aviation guidance.

---

# 4. Knowledge Base & Data Ingestion

## 4.1 Authoritative Source Documents

Initial source documents should include official FAA and government aviation materials.

### Core FAA Sources

- FAA Airman Certification Standards for target certificate/rating
- Pilot’s Handbook of Aeronautical Knowledge
- Airplane Flying Handbook
- Aeronautical Information Manual
- FAR Part 61
- FAR Part 91
- Aviation Weather Handbook
- Risk Management Handbook
- Instrument Flying Handbook, for instrument phase
- Instrument Procedures Handbook, for instrument phase

### Additional Sources to Consider

- FAA advisory circulars relevant to target ACS areas
- FAA safety team publications
- FAA chart users guide
- FAA handbooks on aircraft systems, weather, and aeronautical decision-making
- NTSB safety alerts for scenario/risk-management enrichment

## 4.2 Source Document Strategy

Each ingested document should include metadata:

- Source title
- Source type
- FAA publication number, if available
- Version/date
- URL/source location
- Certificate/rating relevance
- ACS mapping relevance
- Section/chapter/page
- Ingestion date
- Hash/checksum

## 4.3 Ingestion Pipeline

```text
Source Document Acquisition
        ↓
Document Version Storage
        ↓
PDF/Text Parsing
        ↓
Cleaning & Normalization
        ↓
Section Detection
        ↓
Chunking
        ↓
Metadata Tagging
        ↓
Embedding Generation
        ↓
Vector Database Upsert
        ↓
Retrieval Evaluation
```

## 4.4 PDF Parsing

Recommended parsing tools:

- PyMuPDF
- pdfplumber
- Unstructured
- LlamaParse
- Marker

Parsing should preserve:

- Headings
- Page numbers
- Section titles
- Tables where possible
- Figure captions where relevant
- Regulatory numbering

## 4.5 Chunking Strategy

Recommended initial chunking:

- Chunk size: 500–1,000 tokens
- Overlap: 75–150 tokens
- Preserve section boundaries where possible
- Avoid splitting regulatory provisions mid-rule
- Avoid splitting ACS task elements from their labels

### Chunk Types

- ACS task chunks
- Handbook concept chunks
- Regulation chunks
- AIM procedure chunks
- Weather interpretation chunks
- Risk-management guidance chunks

## 4.6 Metadata Tagging

Metadata is critical because ACS alignment is the heart of the product.

Recommended metadata fields:

```json
{
  "source_title": "Private Pilot Airman Certification Standards",
  "source_type": "ACS",
  "publication_date": "TODO",
  "certificate_level": "Private Pilot",
  "category": "Airplane",
  "acs_area_code": "TODO",
  "acs_area_name": "TODO",
  "acs_task_code": "TODO",
  "acs_task_name": "TODO",
  "element_type": "knowledge | risk | skill",
  "page_number": "TODO",
  "section_heading": "TODO",
  "chunk_id": "TODO",
  "document_version": "TODO"
}
```

## 4.7 ACS Mapping

The app should maintain a structured ACS taxonomy table:

- Certificate/rating
- Category/class
- Area of operation
- Task
- Knowledge elements
- Risk-management elements
- Skill elements

This taxonomy should power:

- Study navigation
- Question generation
- Progress tracking
- Weak-area analytics
- Retrieval filters

## 4.8 Embedding Strategy

Each chunk should be embedded with its text plus selected metadata. For example:

```text
Source: Pilot's Handbook of Aeronautical Knowledge
Section: Weather Theory
ACS Mapping: Private Pilot / Preflight Preparation / Weather Information
Text: [chunk content]
```

This improves semantic matching because the embedding carries source and topic context.

## 4.9 Update and Version-Control Strategy

FAA documents may change. The system should support version-aware ingestion.

### Recommended Strategy

- Store every source document version.
- Generate checksums for raw documents.
- Track ingestion date and document publication date.
- Re-ingest changed documents.
- Maintain old chunks for audit history.
- Mark deprecated chunks as inactive rather than deleting immediately.
- Link generated questions to source document version.

### Versioning Example

```text
FAA_PHAK_2024_v1.pdf
FAA_PHAK_2025_v1.pdf
private_pilot_acs_2024_v1.jsonl
private_pilot_acs_2025_v1.jsonl
```

## 4.10 Content Review Workflow

Because aviation accuracy matters, include an expert review path.

Recommended review statuses:

- Generated
- Auto-validated
- Needs expert review
- Approved
- Rejected
- Deprecated

Expert reviewers could include:

- CFI
- Ground instructor
- Instrument instructor
- Aviation curriculum specialist

---

# 5. Prompt Engineering Strategy

## 5.1 Prompting Principles

The LLM should be instructed to:

- Use only retrieved FAA/source context.
- Avoid unsupported claims.
- Cite source chunks used.
- Map every question to ACS metadata when available.
- State uncertainty when context is insufficient.
- Avoid creating fake FAA references.
- Generate educational explanations, not just answer keys.
- Emphasize aeronautical decision-making and risk management.

## 5.2 System Prompt Template

```text
You are an aviation study assistant specialized in FAA Airman Certification Standards preparation.

Your task is to generate accurate, exam-aligned study content using only the retrieved source context provided to you.

Rules:
1. Use only the provided source context. Do not rely on unsupported memory.
2. If the source context is insufficient, say that the context is insufficient and request more relevant material.
3. Do not invent FAA citations, ACS codes, regulations, or handbook references.
4. Every question must be aligned to the provided ACS area/task metadata when available.
5. Every answer explanation must be grounded in the retrieved source material.
6. Prefer practical aviation reasoning over rote memorization.
7. For scenario questions, include realistic pilot decision-making context.
8. For risk-management questions, explicitly identify the hazard, risk, and safe decision logic.
9. Return output in the exact structured format requested.
```

## 5.3 Multiple-Choice Question Prompt Template

```text
Generate one FAA ACS-aligned multiple-choice practice question.

User study goal:
{study_goal}

Target ACS metadata:
{acs_metadata}

Difficulty:
{difficulty}

Retrieved source context:
{retrieved_context}

Output format:
{
  "question_type": "multiple_choice",
  "acs_mapping": {
    "certificate": "",
    "area_of_operation": "",
    "task": "",
    "element_type": "knowledge | risk | skill"
  },
  "question": "",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
    "D": ""
  },
  "correct_answer": "",
  "explanation": "",
  "why_wrong_answers_are_wrong": {
    "A": "",
    "B": "",
    "C": "",
    "D": ""
  },
  "source_references": [],
  "difficulty": "",
  "tags": []
}
```

## 5.4 Scenario-Based Question Prompt Template

```text
Generate one realistic FAA ACS-aligned scenario-based question.

The scenario should require practical aeronautical decision-making, not simple memorization.

User profile:
{user_profile}

Target ACS metadata:
{acs_metadata}

Retrieved source context:
{retrieved_context}

Output format:
{
  "question_type": "scenario_based",
  "scenario": "",
  "question": "",
  "expected_answer": "",
  "grading_rubric": [
    {
      "criterion": "",
      "excellent_response": "",
      "partial_response": "",
      "missing_or_unsafe_response": ""
    }
  ],
  "source_grounded_explanation": "",
  "risk_management_notes": {
    "hazards": [],
    "risks": [],
    "safe_decision_logic": ""
  },
  "acs_mapping": {},
  "source_references": []
}
```

## 5.5 Regulatory Interpretation Prompt Template

```text
Create a regulatory interpretation study question using only the retrieved regulation or FAA guidance context.

Rules:
- Do not provide legal advice.
- Do not invent regulation numbers.
- Make the answer practical for an FAA exam/checkride study context.
- If the retrieved context is insufficient, state that clearly.

Retrieved context:
{retrieved_context}

Output:
{
  "question_type": "regulatory_interpretation",
  "question": "",
  "correct_interpretation": "",
  "common_misunderstanding": "",
  "study_explanation": "",
  "source_references": []
}
```

## 5.6 Free-Response Grading Prompt Template

```text
You are grading a student pilot's free-response answer for FAA ACS study.

Use only the provided retrieved source context and grading rubric.

Question:
{question}

Student answer:
{student_answer}

Retrieved source context:
{retrieved_context}

Rubric:
{rubric}

Return:
{
  "score": 0-100,
  "result": "strong | adequate | needs_review | unsafe_or_incorrect",
  "what_was_correct": [],
  "what_was_missing": [],
  "what_was_incorrect": [],
  "risk_management_feedback": "",
  "recommended_review_topics": [],
  "source_references": []
}
```

## 5.7 Guardrails

### Hallucination Prevention

- Require source references for all explanations.
- Reject outputs with unsupported citations.
- Use post-generation validation to check answer support against retrieved chunks.
- Add “insufficient context” behavior.
- Avoid allowing the LLM to create questions from memory only.

### Safety Guardrails

The app should not present itself as a substitute for:

- A certified flight instructor
- Official FAA publications
- Legal/regulatory counsel
- Aircraft POH/AFM
- Current NOTAM/weather briefing tools

### Output Guardrails

Generated content should be validated for:

- JSON schema compliance
- ACS mapping presence
- Source reference presence
- No invented document titles
- No unsupported regulatory references
- No unsafe aviation advice

## 5.8 Few-Shot Example

### Input Context

```text
ACS Task: Weather Information
Source context explains that pilots must understand weather reports, forecasts, and conditions affecting safe flight.
```

### Desired Output

```json
{
  "question_type": "scenario_based",
  "scenario": "You are planning a daytime VFR cross-country flight and notice lowering ceilings along your route.",
  "question": "What weather information should you review before deciding whether to depart, and what risk-management factors should influence your decision?",
  "expected_answer": "The pilot should review current and forecast weather products relevant to the route and destination, assess ceilings, visibility, trends, alternates, fuel, terrain, pilot proficiency, and whether conditions remain safely within VFR and personal minimums.",
  "source_grounded_explanation": "A complete answer should connect weather information gathering with safe preflight decision-making and risk management.",
  "source_references": ["Retrieved source chunk IDs go here"]
}
```

---

# 6. Development Roadmap

## 6.1 Phase 1 — MVP

### Goal

Build a functional FAA-grounded study app for one certificate/rating path, preferably Private Pilot Airplane.

### Recommended Timeline

**Estimated:** 8–12 weeks for a focused solo developer MVP, depending on polish and review depth.

### Must-Have Features

- User account creation
- Select certificate/rating goal
- Ingest core FAA documents
- Basic ACS taxonomy
- RAG retrieval pipeline
- Multiple-choice question generation
- Explanation with source references
- Basic progress tracking
- Weak-area dashboard
- Admin tool for reviewing generated questions

### MVP Technical Scope

- Next.js frontend
- FastAPI backend
- PostgreSQL + pgvector
- Hosted LLM provider
- Hosted embedding model
- Simple document ingestion CLI
- Basic evaluation dataset

### MVP Success Criteria

- Generates accurate questions grounded in FAA context
- Provides valid source references
- Tracks user performance by topic
- Demonstrates clear improvement over generic chatbot experience
- Can be reviewed by a CFI or aviation subject matter expert

## 6.2 Phase 2 — Expanded Learning Intelligence

### Features

- Instrument Rating content
- Better adaptive learning engine
- Spaced repetition
- Scenario-based oral exam mode
- Free-response grading
- Advanced analytics
- Confidence tracking
- Question quality scoring
- Hybrid retrieval and reranking

### Technical Enhancements

- Reranker model
- Hybrid BM25 + vector search
- Evaluation harness
- Expert review workflow
- Source version comparison
- More granular ACS metadata mapping

## 6.3 Phase 3 — Mobile, Instructor Mode, and Community

### Features

- Mobile app
- Instructor dashboard
- Student assignment workflows
- Study groups
- Shared scenario drills
- CFI-reviewed question packs
- Audio oral-exam practice
- Voice-based answer evaluation

### Business Expansion

- Individual subscription
- Flight school licensing
- Instructor/student bundles
- Premium ACS tracks
- Checkride preparation packages

## 6.4 Phase 4 — Advanced Tutoring System

Potential advanced features:

- Conversational AI tutor
- Mock oral exam simulation
- Personalized checkride readiness score
- Multi-document regulatory reasoning mode
- AI-generated lesson plans for CFI candidates
- Risk-management simulation engine

## 6.5 Deferred Decisions

TODO decisions:

- Which ACS certificate/rating should be MVP?
- Should the app start with written exam prep, checkride prep, or both?
- Should generated questions be saved to a reviewed question bank or generated live every time?
- Should the product initially target individual pilots, instructors, or flight schools?
- What level of source citation detail should be shown to users?
- Should the app support offline/mobile study early?
- What SME review process is required before public launch?

---

# 7. Risks & Open Questions

## 7.1 Legal and Copyright Considerations

Many FAA materials are public domain as U.S. government works, but this should be verified document by document before commercial use.

### Legal TODOs

- Verify public domain status of each FAA source document.
- Confirm rules for using FAA logos or branding.
- Avoid implying FAA endorsement.
- Review terms for any non-FAA sources.
- Add disclaimers that the app is a study aid, not an official FAA product.
- Consult legal counsel before commercial launch.

## 7.2 Hallucination Risk

This is one of the highest product risks.

### Risk

The system may generate incorrect or unsupported aviation explanations that appear authoritative.

### Mitigation

- Use RAG with source grounding.
- Require citations.
- Add output validation.
- Maintain expert-reviewed question bank for high-stakes content.
- Use conservative fallback: “I do not have enough source context.”
- Track user reports of questionable answers.
- Regularly audit generated content.

## 7.3 Retrieval Risk

### Risk

The system may retrieve irrelevant or incomplete context, causing weak or incorrect generated questions.

### Mitigation

- Use ACS metadata filters.
- Improve chunking strategy.
- Add hybrid search.
- Add reranking.
- Build a retrieval evaluation dataset.
- Log retrieval results for review.

## 7.4 Source Update Risk

### Risk

FAA documents may change, and the app may continue using outdated source material.

### Mitigation

- Track document versions.
- Schedule periodic source review.
- Store document publication dates.
- Mark deprecated chunks inactive.
- Re-run evaluation after updates.

## 7.5 Cost at Scale

### Risk

LLM calls for dynamic generation may become expensive as usage grows.

### Mitigation

- Cache generated questions.
- Use reviewed question bank for common topics.
- Use smaller models for simple tasks.
- Use larger models only for scenario generation or grading.
- Limit retrieved context size.
- Monitor cost per session.

## 7.6 Latency Risk

### Risk

RAG + LLM generation may feel slow during study sessions.

### Mitigation

- Pre-generate common questions.
- Stream responses.
- Cache retrieval results.
- Use faster models for basic explanations.
- Generate next question while user reviews current answer.

## 7.7 Aviation Safety Risk

### Risk

Users may over-rely on the app for real-world flight decisions.

### Mitigation

- Clear disclaimers.
- Emphasize training/study use.
- Encourage consultation with CFI and official FAA sources.
- Avoid real-time operational decision support unless future product is designed and reviewed for that purpose.

## 7.8 Open Questions

### Product Questions

- Is the primary product promise written exam prep, oral/checkride prep, or full ACS mastery?
- Should the system generate live questions, maintain a reviewed question bank, or use both?
- Should instructors be part of the first release?
- Will users trust AI-generated questions if they are source-cited?
- What is the minimum expert review needed before launch?

### Technical Questions

- Which vector database gives the best balance of simplicity and retrieval quality?
- Should the system use hybrid search from the beginning?
- Which embedding model performs best on FAA terminology?
- Should ACS mapping be manual, semi-automated, or model-assisted?
- What validation layer is required before showing generated answers?

### Business Questions

- Individual subscription or flight school B2B first?
- Should pricing be per certificate/rating track?
- Should CFI-reviewed premium packs be sold separately?
- What partnerships with flight schools or instructors are feasible?

---

# Recommended MVP Decision Summary

## Product Recommendation

Start with a focused **Private Pilot Airplane ACS study app** that generates source-grounded practice questions, explanations, and scenario drills.

## Architecture Recommendation

Use a **RAG-first architecture** with:

- FastAPI backend
- Next.js frontend
- PostgreSQL + pgvector
- Hosted embedding model
- Hosted LLM provider
- FAA document ingestion pipeline
- ACS metadata tagging
- Basic expert review workflow

## Strategic Reasoning

The product’s trust depends on FAA-grounded accuracy. RAG is the best initial architecture because it provides source traceability, update flexibility, and stronger factual grounding than fine-tuning or generic prompting.

The MVP should avoid overbuilding agentic workflows, mobile apps, and advanced adaptive analytics until the core loop works:

```text
FAA source → retrieval → question → answer → explanation → citation → performance tracking
```

---

# Appendix A — Suggested Repository Structure

```text
faa-acs-study-app/
  apps/
    web/
      app/
      components/
      lib/
  services/
    api/
      app/
        routes/
        rag/
        ingestion/
        prompts/
        evaluation/
        models/
      tests/
  data/
    raw_sources/
    parsed_sources/
    chunks/
    eval_sets/
  docs/
    product/
    architecture/
    prompts/
    ingestion/
  infra/
    docker/
    migrations/
  README.md
```

---

# Appendix B — Suggested Data Models

## User

```text
id
email
name
target_certificate
target_exam_date
created_at
```

## StudySession

```text
id
user_id
session_type
certificate_track
started_at
ended_at
```

## Question

```text
id
question_type
question_text
answer_payload
explanation
acs_area_code
acs_task_code
difficulty
source_chunk_ids
review_status
created_at
```

## QuestionAttempt

```text
id
user_id
question_id
study_session_id
user_answer
is_correct
score
confidence
feedback
created_at
```

## SourceDocument

```text
id
title
source_type
publication_date
version
url
checksum
ingested_at
active
```

## SourceChunk

```text
id
source_document_id
chunk_text
metadata
embedding_id
page_number
section_heading
active
```

---

# Appendix C — Immediate Next Steps

1. Choose the MVP certificate/rating track.
2. Collect official FAA source documents.
3. Build the ACS taxonomy schema.
4. Implement document parsing and chunking.
5. Set up pgvector or another vector database.
6. Create first prompt templates.
7. Generate a small test set of questions.
8. Have an aviation SME review generated outputs.
9. Build the first study session UI.
10. Track performance by ACS area/task.

---

# TODO Markers for v0.2

- TODO: Confirm target MVP certificate/rating.
- TODO: Confirm whether app is written-exam-first or checkride/oral-first.
- TODO: Select exact LLM and embedding provider.
- TODO: Choose vector database based on cost and deployment preference.
- TODO: Confirm list of FAA documents and publication versions.
- TODO: Define expert review process.
- TODO: Add detailed pricing model.
- TODO: Add security/privacy requirements.
- TODO: Add UI wireframe descriptions.
- TODO: Add evaluation benchmark design.
