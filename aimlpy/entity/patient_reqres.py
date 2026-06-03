from pydantic import BaseModel
from typing import Optional


# ── Update patient info ───────────────────────────────────────────────────────
class PatientUpdate(BaseModel):
    full_name:      Optional[str] = None
    age:            Optional[int] = None
    gender:         Optional[str] = None
    contact_number: Optional[str] = None
    address:        Optional[str] = None