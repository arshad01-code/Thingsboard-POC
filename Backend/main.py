from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from db.models import Base
from api import auth, dashboards, devices

app = FastAPI(title="IoT Dashboard SaaS")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(dashboards.router)
app.include_router(devices.router)

@app.get("/")
def root():
    return {"status": "Backend running"}