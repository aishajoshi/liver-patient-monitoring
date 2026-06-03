from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: int
    full_name: str
    email: str
    specialization: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True