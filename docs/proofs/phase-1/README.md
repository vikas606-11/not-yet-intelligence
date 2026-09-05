# Phase 1 Proof

## Backend

```
$ pytest -q
...
17 passed, 25 warnings in 6.69s
```

17/17 tests passing, covering:
- Auth: register (success, duplicate email, short password rejected), login (success, wrong password), `/auth/me` (requires token, returns user)
- Profile: empty get, create + partial update (untouched fields persist), requires auth
- Resumes: upload PDF, reject non-PDF/DOCX, list + delete
- Jobs: create, list, get 404 for missing job, save + idempotent re-save, list saved

Tests run against an isolated SQLite DB — no Postgres dependency for CI/local test runs.

## Frontend

```
$ npm run build
✓ Compiled successfully
✓ Generating static pages (9/9)

Route (app)                              Size     First Load JS
┌ ○ /                                    138 B          87.3 kB
├ ○ /jobs                                2.2 kB         89.4 kB
├ ○ /login                               2 kB           89.2 kB
├ ○ /profile                             2.19 kB        89.4 kB
├ ○ /register                            2.02 kB        89.2 kB
└ ○ /resume                              2 kB           89.2 kB
```

All 5 MVP routes compile cleanly with no type errors.

## End-to-end verification (completed by user, local machine)

- PostgreSQL 17 installed and `jobintel` database configured; backend connected successfully
- Backend running on `localhost:8000`, frontend on `localhost:3000`
- `/healthz` confirmed reachable
- CORS issue found (frontend → backend cross-origin request blocked) and fixed by adding `CORSMiddleware` to `app/main.py`, with allowed origins now configurable via `CORS_ALLOWED_ORIGINS`

Phase 1 is now considered complete.

## MVP boundary check (docs/requirements.md)

| # | Requirement | Status |
|---|---|---|
| 1 | Register | ✓ backend + frontend |
| 2 | Create profile | ✓ backend + frontend |
| 3 | Upload resume | ✓ backend + frontend |
| 4 | Enter job description manually | ✓ backend + frontend |
| 5–9 | Analyze / match / explain | Deferred to Phase 2 (AI), as documented in requirements.md |
| 10 | Save the job | ✓ backend + frontend |
