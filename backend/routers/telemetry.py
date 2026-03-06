from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database_models.database import get_db
from schemas.telemetry import TelemetryPayload
from database_models.models import Telemetry, Device
from services.tb_client import ThingsBoardClient as tb

router = APIRouter()

@router.post("/telemetry")

def ingest(payload: TelemetryPayload, db: Session = Depends(get_db)):

    device = db.query(Device).filter(
        Device.tb_device_id == payload.device_id
    ).first()

    telemetry = Telemetry(
        device_id=device.id,
        temperature=payload.temperature,
        humidity=payload.humidity,
        pressure=payload.pressure
    )

    db.add(telemetry)
    db.commit()

    data = {
        "temperature": payload.temperature,
        "humidity": payload.humidity
    }

    tb.send_telemetry(device.device_token, data)

    return {"status": "ok"}