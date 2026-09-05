from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, jobs, profile, resumes
from app.core.config import settings
from app.core.database import Base, engine
from app import models  # noqa: F401 - ensures models are registered before create_all

app = FastAPI(title="not-yet-intelligence API", version="0.1.0")

# Local dev: frontend (localhost:3000) calling backend (localhost:8000) is a
# cross-origin request. Origins are configurable via settings so production
# can restrict this to the real deployed frontend domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    # Phase 1: create_all for local dev speed. Alembic migrations are the
    # source of truth going forward (see alembic/ and README) once schema
    # changes start happening after the initial MVP.
    Base.metadata.create_all(bind=engine)


@app.get("/healthz", tags=["health"])
def healthz():
    return {"status": "ok"}


app.include_router(auth.router, prefix="/api/v1")
app.include_router(profile.router, prefix="/api/v1")
app.include_router(resumes.router, prefix="/api/v1")
app.include_router(jobs.router, prefix="/api/v1")
