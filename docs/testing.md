# Testing Strategy

Test actual business behavior — not coverage numbers.

## Backend (FastAPI)

- **Unit tests:** service-layer logic (validation, scoring rules once they exist, business rules) — pytest
- **Integration tests:** API endpoints against a test database (register → login → profile → resume upload → job create → save)
- **Contract:** request/response schemas match `docs/api.md`

## Frontend (Next.js)

- Component tests for forms (registration, profile, resume upload) once built
- Basic e2e for the MVP happy path (Phase 1 end): register → profile → upload resume → add job → save job

## Later phases

- AI service: prompt/response contract tests with mocked Bedrock responses (Phase 2)
- Matching engine: deterministic scoring tests with fixed inputs/expected outputs (Phase 2)
- Deduplication: known-duplicate and known-distinct job pairs (Phase 3)
- Container scanning (Trivy) and static analysis (SonarQube) added to CI (Phase 7)

## What we do NOT do

- Write tests solely to inflate coverage percentage
- Test framework internals or third-party libraries
- Skip tests for "simple" auth/security-relevant code — these are always tested
