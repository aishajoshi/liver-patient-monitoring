from sqlalchemy.orm import Session
from repo.patient_repo import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
    update_patient,
    delete_patient
)
from entity.patient import PatientCreate, PatientResponse
from entity.patient_reqres import PatientUpdate


# ── Add a new patient ─────────────────────────────────────────────────────────
def add_patient(db: Session, patient: PatientCreate) -> PatientResponse:
    saved = create_patient(db, patient)
    return PatientResponse.from_orm(saved)


# ── Get all patients ──────────────────────────────────────────────────────────
def fetch_all_patients(db: Session) -> list:
    patients = get_all_patients(db)
    return [PatientResponse.from_orm(p) for p in patients]


# ── Get one patient by ID ─────────────────────────────────────────────────────
def fetch_patient(db: Session, patient_id: int) -> PatientResponse:
    patient = get_patient_by_id(db, patient_id)
    if not patient:
        return None
    return PatientResponse.from_orm(patient)


# ── Update patient details ────────────────────────────────────────────────────
def modify_patient(db: Session, patient_id: int, data: PatientUpdate) -> PatientResponse:
    updated = update_patient(db, patient_id, data.dict(exclude_none=True))
    if not updated:
        return None
    return PatientResponse.from_orm(updated)


# ── Delete a patient ──────────────────────────────────────────────────────────
def remove_patient(db: Session, patient_id: int) -> bool:
    return delete_patient(db, patient_id)