from fastapi import APIRouter
from schema.device import DeviceCreate
import uuid

router = APIRouter(prefix="/devices", tags=["Devices"])

@router.post("/provision")
def provision_device(device: DeviceCreate):

    access_token = str(uuid.uuid4())

    return {
        "device_name": device.name,
        "device_type": device.type,
        "access_token": access_token
    }