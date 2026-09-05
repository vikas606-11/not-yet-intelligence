from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.job import Job
from app.models.saved_job import SavedJob
from app.models.user import User
from app.schemas.job import JobIn, JobOut, SavedJobOut

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("", response_model=JobOut, status_code=status.HTTP_201_CREATED)
def create_job(payload: JobIn, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    job = Job(created_by=current_user.id, source="manual", **payload.model_dump())
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


@router.get("", response_model=list[JobOut])
def list_jobs(db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.status == "active").order_by(Job.created_at.desc()).all()


@router.get("/saved", response_model=list[SavedJobOut])
def list_saved_jobs(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(SavedJob).filter(SavedJob.user_id == current_user.id).all()


@router.get("/{job_id}", response_model=JobOut)
def get_job(job_id: str, db: Session = Depends(get_db)):
    job = db.get(Job, job_id)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return job


@router.post("/{job_id}/save", response_model=SavedJobOut, status_code=status.HTTP_201_CREATED)
def save_job(job_id: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    job = db.get(Job, job_id)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")

    existing = (
        db.query(SavedJob)
        .filter(SavedJob.user_id == current_user.id, SavedJob.job_id == job_id)
        .first()
    )
    if existing:
        return existing

    saved = SavedJob(user_id=current_user.id, job_id=job_id)
    db.add(saved)
    db.commit()
    db.refresh(saved)
    return saved
