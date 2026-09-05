from pydantic import BaseModel


class ProfileIn(BaseModel):
    name: str | None = None
    experience_years: float | None = None
    location: str | None = None
    preferred_locations: list[str] | None = None
    target_roles: list[str] | None = None
    skills: list[str] | None = None
    education: str | None = None
    career_goals: str | None = None
    work_preference: str | None = None
    salary_preference: str | None = None


class ProfileOut(ProfileIn):
    id: str
    user_id: str

    class Config:
        from_attributes = True
