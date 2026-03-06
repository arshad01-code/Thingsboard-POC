from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database_models.database import get_db
from database_models.models import Device, Telemetry

router = APIRouter()

@router.get("/analytics/device/{device_id}")

def device_stats(device_id: str, db: Session = Depends(get_db)):

    device = db.query(Device).filter(
        Device.tb_device_id == device_id
    ).first()

    data = db.query(
        func.avg(Telemetry.temperature),
        func.max(Telemetry.temperature),
        func.min(Telemetry.temperature)
    ).filter(
        Telemetry.device_id == device.id
    ).first()

    return {
        "avg_temperature": data[0],
        "max_temperature": data[1],
        "min_temperature": data[2]
    }