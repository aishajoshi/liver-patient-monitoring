from .setting import Base, engine
from aimlpy.model.user_report import User


print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
