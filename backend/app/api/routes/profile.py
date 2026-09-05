from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.profile import Profile
from app.models.user import User
from app.schemas.profile import ProfileIn, ProfileOut

router = APIRouter(prefix="/profile", tags=["profile"])


@router.get("", response_model=ProfileOut | None)
def get_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Profile).filter(Profile.user_id == current_user.id).first()


@router.put("", response_model=ProfileOut)
def upsert_profile(
    payload: ProfileIn,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    data = payload.model_dump(exclude_unset=True)

    if profile:
        for field, value in data.items():
            setattr(profile, field, value)
    else:
        profile = Profile(user_id=current_user.id, **data)
        db.add(profile)

    db.commit()
    db.refresh(profile)
    return profile
