# PROJECT_STATUS

Current Phase: Phase 0 — Planning & Documentation
Current Phase: Phase 1 — MVP (COMPLETE)
Current Task: None — Phase 1 closed, awaiting "Start Phase 2"
Completed:
- Phase 0: full documentation set (see prior tag v0.1-phase-0)
- Backend (FastAPI modular monolith): auth, profile, resumes, jobs, saved_jobs
  - Models match docs/database.md MVP schema
  - Endpoints match docs/api.md MVP scope
  - JWT auth, bcrypt password hashing
  - Local-disk resume storage behind a swappable interface (app/services/storage.py)
  - Alembic scaffolded (not yet used — Phase 1 relies on create_all locally)
  - 17/17 pytest tests passing (isolated SQLite, no Postgres needed for tests)
  - Fixed bcrypt 5.x/passlib incompatibility by pinning bcrypt==4.0.1
- Frontend (Next.js + TypeScript): register, login, profile, resume, jobs pages
  - Typed API client (lib/api.ts) against backend /api/v1
  - `npm run build` verified clean (all 5 routes compile)
- CORS middleware added (app/main.py) — required for frontend :3000 to call backend :8000; allowed origins configurable via CORS_ALLOWED_ORIGINS
- Verified locally by user: PostgreSQL 17 + jobintel DB connected, backend :8000 and frontend :3000 running, /healthz confirmed, CORS issue found and fixed
In Progress:
- None
Blocked:
- None
Next Task:
- Wait for "Start Phase 2" (AI/Bedrock integration: job analysis, resume parsing, match scoring, explainable output)
Architecture Decisions:
- Modular monolith first (see docs/decisions/0001-modular-monolith.md)
- AI isolated behind internal AI service (replaceable provider) — not yet built, Phase 2
- Code calculates match scores deterministically; AI explains/interprets semantically — not yet built, Phase 2
- Resume storage: local disk (Phase 1) behind swappable interface, S3 later — documented deviation from architecture.md diagram
Known Issues:
- bcrypt>=5.0 breaks passlib's version probe; pinned to bcrypt==4.0.1 in backend/requirements.txt
- No refresh-token flow yet (single access token, matches Phase 1 scope)
- Resume parsing (parsed_data) not populated — Phase 2 (AI)
- CORS origins default to localhost:3000/127.0.0.1:3000 only; update CORS_ALLOWED_ORIGINS when deploying frontend elsewhere
Architecture Decisions:
- Modular monolith first (see docs/decisions/0001-modular-monolith.md)
- AI isolated behind internal AI service (replaceable provider)
- Code calculates match scores deterministically; AI explains/interprets semantically
Known Issues:
- None yet
