# Database Design

Primary database: **PostgreSQL**. Large files (resume PDFs/DOCX) go to **S3**, never stored as blobs in Postgres.

## Scope note

This doc defines the **full target entity list** (for reference) and the **MVP schema** (what Phase 1 actually creates). Only the MVP schema should be migrated in Phase 1.

## Full target entities (reference, not all built in MVP)

`users, profiles, skills, resumes, jobs, companies, job_skills, job_sources, job_analysis, job_matches, applications, notifications`

## MVP schema (Phase 1)

```
users
├── id            uuid PK
├── email         text unique not null
├── password_hash text not null
├── created_at    timestamptz default now()
└── updated_at    timestamptz

profiles
├── id                 uuid PK
├── user_id            uuid FK -> users.id, unique
├── name               text
├── experience_years   numeric
├── location           text
├── preferred_locations text[]
├── target_roles       text[]
├── skills             text[]
├── education          text
├── career_goals       text
├── work_preference     text        -- remote/hybrid/onsite
├── salary_preference   text
├── created_at         timestamptz default now()
└── updated_at          timestamptz

resumes
├── id            uuid PK
├── user_id       uuid FK -> users.id
├── file_url      text not null      -- S3 key/URL
├── file_type     text               -- pdf | docx
├── uploaded_at   timestamptz default now()
└── parsed_data   jsonb              -- populated once parsing exists (Phase 1 stub / Phase 2 real)

jobs
├── id                  uuid PK
├── title               text not null
├── company             text
├── description         text not null
├── location            text
├── employment_type     text
├── experience_required text
├── salary              text
├── skills              text[]
├── source              text default 'manual'
├── source_url          text
├── posted_date         date
├── collected_date       timestamptz default now()
├── status              text default 'active'
├── created_by          uuid FK -> users.id
└── created_at          timestamptz default now()

saved_jobs
├── id        uuid PK
├── user_id   uuid FK -> users.id
├── job_id    uuid FK -> jobs.id
├── status    text default 'saved'   -- saved | applied | interview | rejected | offer
└── saved_at  timestamptz default now()
```

## Deferred to Phase 2+

- `job_analysis` (AI output: role, seniority, required/preferred skills, responsibilities, tools, domain)
- `job_matches` (match score + explanation)
- `companies`, `job_skills` (normalized skill taxonomy), `job_sources` (multi-source Phase 3)
- `notifications` (Phase 4)

## Relationships (MVP)

- `users` 1—1 `profiles`
- `users` 1—N `resumes`
- `users` 1—N `jobs` (as creator, manual input)
- `users` N—N `jobs` via `saved_jobs`

## Indexing notes (MVP)

- `users.email` unique index
- `saved_jobs (user_id, job_id)` unique composite index
- `jobs.status`, `jobs.created_by` indexed for common queries
