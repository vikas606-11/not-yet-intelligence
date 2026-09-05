# Backend — not-yet-intelligence

FastAPI modular monolith. Phase 1 (MVP) scope: auth, profile, resumes, manual job input/saving.
See `../docs/api.md` and `../docs/database.md` for the full contract.

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then set a real DATABASE_URL / JWT_SECRET
```

Requires a running PostgreSQL instance matching `DATABASE_URL` (or use Docker — added in Phase 5).

## Run

```bash
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs
Health check: http://localhost:8000/healthz

Tables are created automatically on startup for Phase 1 (`Base.metadata.create_all`). Alembic (`alembic/`) is set up as the migration path forward once schema changes start happening post-MVP.

## Test

```bash
pytest -q
```

Tests run against an isolated SQLite database (`tests/conftest.py`) — no Postgres needed to run the suite.

## Structure

```
app/
├── core/        config, db session, security (hashing, JWT)
├── models/      SQLAlchemy models (users, profiles, resumes, jobs, saved_jobs)
├── schemas/     Pydantic request/response models
├── api/routes/  auth, profile, resumes, jobs
├── services/    storage.py (local-disk resume storage, S3-swappable later)
└── main.py      app entrypoint, router registration
```

## Notes / deviations from docs

- Resume files are stored on local disk (`storage/resumes/`, gitignored) behind `app/services/storage.py` rather than S3. The interface is designed so S3 can replace it later without touching callers. See `PROJECT_STATUS.md`.
- Resume **parsing** (`parsed_data`) is not populated yet — that's Phase 2 (AI).
