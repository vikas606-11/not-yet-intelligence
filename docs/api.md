# API Design

FastAPI, modular monolith. Base path: `/api/v1`.

## Scope note

Only MVP (Phase 1) endpoints are specified in detail below. Matching/AI/jobs-aggregation endpoints are placeholders for Phase 2/3 and will be filled in when those phases start.

## Auth

| Method | Path | Description |
|---|---|---|
| POST | `/auth/register` | Create user (email, password) |
| POST | `/auth/login` | Returns JWT access token |
| POST | `/auth/refresh` | Refresh access token |
| GET | `/auth/me` | Current authenticated user |

## Profile

| Method | Path | Description |
|---|---|---|
| GET | `/profile` | Get current user's profile |
| PUT | `/profile` | Create/update profile |

## Resume

| Method | Path | Description |
|---|---|---|
| POST | `/resumes` | Upload resume (PDF/DOCX) → stored in S3, row created |
| GET | `/resumes` | List current user's resumes |
| GET | `/resumes/{id}` | Get resume metadata |
| DELETE | `/resumes/{id}` | Delete resume |

> Resume **parsing** (extracting structured data) is Phase 2 — the `parsed_data` field exists in the schema but is not populated by Phase 1 endpoints.

## Jobs (manual input only in MVP)

| Method | Path | Description |
|---|---|---|
| POST | `/jobs` | Manually add a job description |
| GET | `/jobs` | List jobs (own + public manual entries) |
| GET | `/jobs/{id}` | Get job detail |
| POST | `/jobs/{id}/save` | Save a job (creates `saved_jobs` row) |
| GET | `/jobs/saved` | List current user's saved jobs |

## Deferred (documented for future phases, not built yet)

- `POST /jobs/{id}/analyze` — AI job analysis (Phase 2)
- `GET /jobs/{id}/match` — resume-vs-job match score + explanation (Phase 2)
- `GET /market/skills` — market skill intelligence (Phase 3)
- `GET /career/actions` — career action engine output (Phase 3)
- `PATCH /applications/{id}/status` — application status transitions (Phase 4)
- `GET /dashboard` — application tracker dashboard (Phase 4)

## Conventions

- All endpoints under `/api/v1` except health checks (`/healthz`)
- Auth via `Authorization: Bearer <JWT>`
- Standard error shape: `{"error": {"code": str, "message": str}}`
- Pagination via `?page=&page_size=` on list endpoints
