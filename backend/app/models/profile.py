import uuid
from datetime import datetime, timezone

from sqlalchemy import String, DateTime, Numeric, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), unique=True, nullable=False)

    name: Mapped[str | None] = mapped_column(String, nullable=True)
    experience_years: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    location: Mapped[str | None] = mapped_column(String, nullable=True)
    preferred_locations: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
    target_roles: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
    skills: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
    education: Mapped[str | None] = mapped_column(String, nullable=True)
    career_goals: Mapped[str | None] = mapped_column(String, nullable=True)
    work_preference: Mapped[str | None] = mapped_column(String, nullable=True)
    salary_preference: Mapped[str | None] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )

    user = relationship("User", back_populates="profile")
