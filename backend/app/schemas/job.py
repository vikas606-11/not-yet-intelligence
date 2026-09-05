from datetime import date, datetime

from pydantic import BaseModel


class JobIn(BaseModel):
    title: str
    company: str | None = None
    description: str
    location: str | None = None
    employment_type: str | None = None
    experience_required: str | None = None
    salary: str | None = None
    skills: list[str] | None = None
    source_url: str | None = None
    posted_date: date | None = None


class JobOut(BaseModel):
    id: str
    title: str
    company: str | None
    description: str
    location: str | None
    employment_type: str | None
    experience_required: str | None
    salary: str | None
    skills: list[str] | None
    source: str
    source_url: str | None
    posted_date: date | None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class SavedJobOut(BaseModel):
    id: str
    job_id: str
    status: str

    class Config:
        from_attributes = True
