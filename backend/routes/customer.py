from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Customer
from services.thingsboard import tb_request

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Customer
@router.post("/")
def create_customer(name: str, db: Session = Depends(get_db)):

    # Create in ThingsBoard
    tb_customer = tb_request(
        "POST",
        "/api/customer",
        json={"title": name}
    )

    # Store in PostgreSQL
    customer = Customer(
        name=name,
        tb_customer_id=tb_customer["id"]["id"]
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


# Delete Customer
@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):

    customer = db.query(Customer).get(customer_id)

    if not customer:
        raise HTTPException(status_code=404)

    # Delete in ThingsBoard
    tb_request("DELETE", f"/api/customer/{customer.tb_customer_id}")

    db.delete(customer)
    db.commit()

    return {"message": "Customer deleted"}