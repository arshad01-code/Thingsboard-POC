from fastapi import APIRouter, Depends
from services.tb_client import ThingsBoardClient

from sqlalchemy.orm import Session

from database_models.database import get_db
from database_models.models import Device
from schemas.devices import DeviceCreateSchema

router = APIRouter()

tb = ThingsBoardClient()

@router.post("/devices")
def create_device(
    device: DeviceCreateSchema,
    db: Session = Depends(get_db)
):
    device_id, device_type = tb.create_device(device.name)
    new_device: Device = Device(
        name=device.name,
        tb_device_id=device_id,
        type=device_type
    )
    db.add(new_device)
    db.commit()
    db.refresh(new_device)