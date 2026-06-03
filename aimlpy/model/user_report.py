from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from aimlpy.setting import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    specialization = Column(String(100))  # e.g. Hepatologist, General Physician
    created_at = Column(DateTime(timezone=True), server_default=func.now())
