from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.config import settings
from app.core.database import get_db
from app.models.resume import Resume
from app.models.user import User
from app.schemas.resume import ResumeOut
from app.services import storage

router = APIRouter(prefix="/resumes", tags=["resumes"])

_TYPE_MAP = {
    "application/pdf": "pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
}


@router.post("", response_model=ResumeOut, status_code=status.HTTP_201_CREATED)
async def upload_resume(
    file: UploadFile,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if file.content_type not in settings.resume_allowed_types:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF or DOCX files are allowed")

    content = await file.read()
    max_bytes = settings.resume_max_size_mb * 1024 * 1024
    if len(content) > max_bytes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File exceeds {settings.resume_max_size_mb}MB limit",
        )

    file_url = storage.save_resume(current_user.id, file.filename or "resume", content)
    resume = Resume(user_id=current_user.id, file_url=file_url, file_type=_TYPE_MAP[file.content_type])
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume


@router.get("", response_model=list[ResumeOut])
def list_resumes(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Resume).filter(Resume.user_id == current_user.id).all()


@router.get("/{resume_id}", response_model=ResumeOut)
def get_resume(resume_id: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    resume = _get_owned_resume(resume_id, current_user, db)
    return resume


@router.delete("/{resume_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resume(resume_id: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    resume = _get_owned_resume(resume_id, current_user, db)
    storage.delete_resume(resume.file_url)
    db.delete(resume)
    db.commit()


def _get_owned_resume(resume_id: str, current_user: User, db: Session) -> Resume:
    resume = db.get(Resume, resume_id)
    if not resume or resume.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resume not found")
    return resume
