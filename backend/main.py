from fastapi import FastAPI
from database_models.database import Base, engine
from routers import devices, dashboards, customers, telemetry, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Vincrus POC')

app.include_router(devices.router)
app.include_router(dashboards.router)
app.include_router(customers.router)
app.include_router(telemetry.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"status": "Platform running"}