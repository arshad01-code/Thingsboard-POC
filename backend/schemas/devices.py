from pydantic import BaseModel

class DeviceCreateSchema(BaseModel):
    name: str
    type: str = "default"
