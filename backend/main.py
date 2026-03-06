from fastapi import FastAPI
from database_models.database import Base, engine
from routers import devices, dashboards, customers

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Vincrus POC')

app.include_router(devices.router)
app.include_router(dashboards.router)
app.include_router(customers.router)

@app.get("/")
def root():
    return {"status": "Platform running"}