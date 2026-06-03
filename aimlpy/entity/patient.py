from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ── Create patient (what doctor fills in the form) ────────────────────────────
class PatientCreate(BaseModel):
    full_name:      str
    age:            int
    gender:         str          # Male / Female / Other
    contact_number: Optional[str] = None
    address:        Optional[str] = None
    registered_by:  Optional[int] = None   # doctor's user id


# ── Patient response (what we send back after saving) ────────────────────────
class PatientResponse(BaseModel):
    id:             int
    full_name:      str
    age:            int
    gender:         str
    contact_number: Optional[str] = None
    address:        Optional[str] = None
    registered_by:  Optional[int] = None
    created_at:     Optional[datetime] = None

    class Config:
        from_attributes = True