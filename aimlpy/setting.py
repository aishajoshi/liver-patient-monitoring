from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres@localhost:5432/liver_monitoring_system"
#                                      ↑ change this to your PostgreSQL password
API_PORT = 8000

# ── SQLAlchemy Engine ─────────────────────────────────────────────────────────
engine = create_engine(DATABASE_URL, echo=True)
# echo=True prints SQL queries in terminal (helpful while learning)

# ── Session Factory ───────────────────────────────────────────────────────────
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ── Base class for all models ─────────────────────────────────────────────────
Base = declarative_base()


# ── Helper: get a DB session ──────────────────────────────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
