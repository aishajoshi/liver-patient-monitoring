from sqlalchemy import (
    Column, Integer, String, Numeric, Boolean,
    Text, DateTime, ForeignKey, CheckConstraint
)
from sqlalchemy.sql import func
from setting import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    specialization = Column(String(100))  # e.g. Hepatologist, General Physician
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# ── 2. PATIENTS TABLE ─────────────────────────────────────────────────────────
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(20))
    address = Column(Text)
    registered_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        CheckConstraint("age > 0 AND age < 130", name="check_age"),
        CheckConstraint("gender IN ('Male', 'Female', 'Other')", name="check_gender"),
    )


# ── 3. LIVER REPORTS TABLE ────────────────────────────────────────────────────
#    Lab values from Indian Liver Patient Dataset (ILPD)
#    + risk score and risk tier included directly
class LiverReport(Base):
    __tablename__ = "liver_reports"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"), nullable=False)
    recorded_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    # Bilirubin
    total_bilirubin = Column(Numeric(6, 2))  # mg/dL
    direct_bilirubin = Column(Numeric(6, 2))  # mg/dL

    # Liver enzymes
    alkaline_phosphotase = Column(Integer)  # IU/L
    alamine_aminotransferase = Column(Integer)  # IU/L  (SGPT)
    aspartate_aminotransferase = Column(Integer)  # IU/L  (SGOT)

    # Proteins
    total_proteins = Column(Numeric(5, 2))  # g/dL
    albumin = Column(Numeric(5, 2))  # g/dL
    albumin_globulin_ratio = Column(Numeric(5, 2))

    # ML model prediction
    is_liver_patient = Column(Boolean)  # True = liver disease predicted

    # Risk score (0–100) and tier — stored directly in this table
    risk_score = Column(Numeric(5, 2))  # 0.00 – 100.00
    risk_tier = Column(String(20))  # Low / Moderate / High / Critical

    report_date = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        CheckConstraint("risk_score >= 0 AND risk_score <= 100", name="check_risk_score"),
        CheckConstraint("risk_tier IN ('Low', 'Moderate', 'High', 'Critical')", name="check_risk_tier"),
    )
