from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Device
from services.thingsboard import tb_request

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Device
@router.post("/")
def create_device(name: str, db: Session = Depends(get_db)):

    # Create in ThingsBoard
    tb_device = tb_request(
        "POST",
        "/api/device",
        json={"name": name, "type": "default"}
    )

    device_id = tb_device["id"]["id"]

    # Get credentials (token)
    credentials = tb_request(
        "GET",
        f"/api/device/{device_id}/credentials"
    )

    # Store in PostgreSQL
    device = Device(
        name=name,
        tb_device_id=device_id,
        tb_device_token=credentials["credentialsId"]
    )

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


# Delete Device
@router.delete("/{device_id}")
def delete_device(device_id: int, db: Session = Depends(get_db)):

    device = db.query(Device).get(device_id)

    if not device:
        raise HTTPException(status_code=404)

    tb_request("DELETE", f"/api/device/{device.tb_device_id}")

    db.delete(device)
    db.commit()

    return {"message": "Device deleted"}