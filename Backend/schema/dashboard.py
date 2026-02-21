from pydantic import BaseModel
from typing import List, Dict, Any

class Widget(BaseModel):
    type: str
    title: str
    telemetry_key: str
    x_axis: int
    y_axis: int
    width: int
    height: int

class DashboardRequest(BaseModel):
    host: str
    email: str
    password: str
    widgets: List[Widget]