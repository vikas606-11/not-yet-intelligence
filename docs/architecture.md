# Architecture

## High-level architecture (target, full product)

```
USERS
  │
  ▼
Web Application (Next.js)
  │
  ▼
API Gateway
  │
  ┌──────────────┼──────────────┐
  ▼              ▼              ▼
User Service  Job Service   AI Service
  │              │              │
  │              │              ▼
  │              │         Amazon Bedrock
  │              │
  └──────────────┼──────────────┐
                 ▼               ▼
             PostgreSQL        Redis
                 │
                 ▼
                 S3
```

## MVP architecture (Phase 1)

```
Next.js (frontend)
     │  HTTP/JSON
     ▼
FastAPI (modular monolith)
 ├── auth
 ├── users / profiles
 ├── resumes
 └── jobs (manual input only)
     │
     ▼
PostgreSQL          S3 (resume files)
```

No Redis, no queue, no AI service, no Bedrock call in Phase 1. Those are introduced in Phase 2+ as the relevant features are built — see `development-roadmap.md`.

## Backend structure (modular monolith)

```
FastAPI
 ├── authentication
 ├── users
 ├── profiles
 ├── resumes
 ├── jobs
 ├── matching
 ├── ai
 └── applications
```

Each module is self-contained (own routes, schemas, service logic) so it can be extracted into a separate service later without a rewrite. See `decisions/0001-modular-monolith.md`.

## AI architecture (introduced Phase 2)

```
Application
    ↓
AI Service (internal interface)
    ↓
Prompt Builder
    ↓
Amazon Bedrock
    ↓
Structured Output
```

The AI service is the only module allowed to call Bedrock. This keeps the provider replaceable:

```
AI Service
├── Amazon Bedrock   (default)
├── Local Model      (future option)
└── Other Provider   (future option)
```

**Principle: Code calculates, AI understands and explains.** Deterministic code owns filtering, sorting, exact skill matching, experience/location/salary/date comparison, and scoring rules. AI owns semantic understanding, skill extraction, similar-technology recognition, job interpretation, match explanation, and career recommendations.

## Job ingestion architecture (introduced Phase 3)

```
JOB SOURCES (APIs/feeds, company pages, user URLs)
        │
        ▼
  Source Adapters
        │
        ▼
   Normalization
        │
        ▼
       SQS
        │
        ▼
 Processing Workers
   ├── Duplicate Detection
   └── AI Analysis
        │
        ▼
     Database
```

Source adapters are independently addable/removable. Only authorized APIs, public feeds, permitted career pages/ATS platforms, and user-submitted URLs are supported — no scraping that bypasses restrictions.

## Cloud/DevOps architecture (introduced Phase 5+)

Deferred until the relevant phase. Full target-state diagrams (Kubernetes, GitOps, AWS production architecture) live in the project specification and will be copied into `deployment.md` when Phase 6–8 begin, not implemented now.
