from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import CustomerDevice

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Map Device to Customer
@router.post("/customers/{customer_id}/devices/{device_id}")
def map_device(customer_id: int, device_id: int, db: Session = Depends(get_db)):

    mapping = CustomerDevice(
        customer_id=customer_id,
        device_id=device_id
    )

    db.add(mapping)
    db.commit()

    return {"message": "Device mapped"}


# Unmap
@router.delete("/customers/{customer_id}/devices/{device_id}")
def unmap_device(customer_id: int, device_id: int, db: Session = Depends(get_db)):

    mapping = db.query(CustomerDevice).filter_by(
        customer_id=customer_id,
        device_id=device_id
    ).first()

    if not mapping:
        raise HTTPException(status_code=404)

    db.delete(mapping)
    db.commit()

    return {"message": "Device unmapped"}