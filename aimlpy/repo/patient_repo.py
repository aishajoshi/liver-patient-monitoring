from sqlalchemy.orm import Session
from model.patient_record import PatientRecord
from entity.patient import PatientCreate


def create_patient(db: Session, patient: PatientCreate) -> PatientRecord:
    new_patient = PatientRecord(
        full_name      = patient.full_name,
        age            = patient.age,
        gender         = patient.gender,
        contact_number = patient.contact_number,
        address        = patient.address,
        registered_by  = patient.registered_by
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


def get_all_patients(db: Session) -> list:
    return db.query(PatientRecord).all()


def get_patient_by_id(db: Session, patient_id: int) -> PatientRecord:
    return db.query(PatientRecord).filter(PatientRecord.id == patient_id).first()


def update_patient(db: Session, patient_id: int, updated_data: dict) -> PatientRecord:
    patient = db.query(PatientRecord).filter(PatientRecord.id == patient_id).first()
    if patient:
        for key, value in updated_data.items():
            if value is not None:
                setattr(patient, key, value)
        db.commit()
        db.refresh(patient)
    return patient


def delete_patient(db: Session, patient_id: int) -> bool:
    patient = db.query(PatientRecord).filter(PatientRecord.id == patient_id).first()
    if patient:
        db.delete(patient)
        db.commit()
        return True
    return False