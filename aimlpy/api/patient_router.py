from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from setting import get_db
from entity.patient import PatientCreate, PatientResponse
from entity.patient_reqres import PatientUpdate
from entity.common import SuccessResponse, ErrorResponse
from service.patient_service import (
    add_patient,
    fetch_all_patients,
    fetch_patient,
    modify_patient,
    remove_patient
)

router = APIRouter(prefix="/patients", tags=["Patients"])


# ── Add new patient ───────────────────────────────────────────────────────────
@router.post("/add", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return add_patient(db, patient)


# ── Get all patients ──────────────────────────────────────────────────────────
@router.get("/all", response_model=list[PatientResponse])
def get_all(db: Session = Depends(get_db)):
    return fetch_all_patients(db)


# ── Get one patient by ID ─────────────────────────────────────────────────────
@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = fetch_patient(db, patient_id)
    if not patient:
        return ErrorResponse(message=f"Patient with ID {patient_id} not found")
    return patient


# ── Update patient ────────────────────────────────────────────────────────────
@router.put("/update/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, data: PatientUpdate, db: Session = Depends(get_db)):
    updated = modify_patient(db, patient_id, data)
    if not updated:
        return ErrorResponse(message=f"Patient with ID {patient_id} not found")
    return updated


# ── Delete patient ────────────────────────────────────────────────────────────
@router.delete("/delete/{patient_id}", response_model=SuccessResponse)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    deleted = remove_patient(db, patient_id)
    if not deleted:
        return ErrorResponse(message=f"Patient with ID {patient_id} not found")
    return SuccessResponse(message="Patient deleted successfully")