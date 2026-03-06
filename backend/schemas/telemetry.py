from pydantic import BaseModel

class TelemetryPayload(BaseModel):

    device_id: str
    temperature: float | None = None
    humidity: float | None = None
    pressure: float | None = None