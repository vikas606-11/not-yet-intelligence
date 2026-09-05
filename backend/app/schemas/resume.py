from datetime import datetime

from pydantic import BaseModel


class ResumeOut(BaseModel):
    id: str
    file_type: str
    uploaded_at: datetime

    class Config:
        from_attributes = True
