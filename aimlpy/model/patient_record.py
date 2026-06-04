from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.sql import func
from setting import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id             = Column(Integer, primary_key=True, index=True)
    full_name      = Column(String(100), nullable=False)
    email          = Column(String(150), unique=True, nullable=False)
    password_hash  = Column(String(255), nullable=False)
    specialization = Column(String(100))
    created_at     = Column(DateTime(timezone=True), server_default=func.now())


class PatientRecord(Base):
    __tablename__ = "patients"
    __table_args__ = (
        CheckConstraint("age > 0 AND age < 130", name="check_age"),
        CheckConstraint("gender IN ('Male', 'Female', 'Other')", name="check_gender"),
        {"extend_existing": True}
    )

    id             = Column(Integer, primary_key=True, index=True)
    full_name      = Column(String(100), nullable=False)
    age            = Column(Integer, nullable=False)
    gender         = Column(String(10), nullable=False)
    contact_number = Column(String(20))
    address        = Column(Text)
    registered_by  = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at     = Column(DateTime(timezone=True), server_default=func.now())