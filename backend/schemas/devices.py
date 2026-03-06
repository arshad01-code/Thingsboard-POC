from uuid import UUID

from pydantic import BaseModel

class DeviceCreateSchema(BaseModel):
    name: str
    type: str = "default"
    customer_id: UUID
