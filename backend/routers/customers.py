from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.tb_client import ThingsBoardClient

from database_models.database import get_db
from database_models.models import Customer
from schemas.customers import CustomerCreateSchema

router = APIRouter()

tb = ThingsBoardClient()

@router.post("/customer")
def create_customer(
    customer: CustomerCreateSchema,
    db: Session = Depends(get_db)
):
    new_cust_id =  tb.create_tb_customer(
        customer_name=customer.name,
        email=customer.email
    )
    new_cust: Customer = Customer(
        name=customer.name,
        tb_customer_id=new_cust_id,
        email=customer.email
    )
    db.add(new_cust)
    db.commit()
    db.refresh(new_cust)

    return new_cust


@router.get("/customers/{customer_name}")

def get_customers(
    customer_name: str,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer).filter(
        Customer.name == customer_name
    ).first()

    if not customer:
        return {"error": "Customer not found"}

    return customer