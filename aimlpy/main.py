from fastapi import FastAPI
from api.patient_router import router as patient_router

app = FastAPI(
    title="Liver Patient Monitoring System",
    description="A system for monitoring liver patients using ML and risk scoring",
    version="1.0.0"
)

app.include_router(patient_router)

@app.get("/")
def root():
    return {"message": "Liver Patient Monitoring System is running!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)