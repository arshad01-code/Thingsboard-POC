from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

from routes.customer import router as customer_router
from routes.device import router as device_router
from routes.customer_device import router as mapping_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(customer_router, prefix="/customers", tags=["Customers"])
app.include_router(device_router, prefix="/devices", tags=["Devices"])
app.include_router(mapping_router, tags=["Mapping"])

@app.get("/")
def root():
    return {"status": "Backend running"}