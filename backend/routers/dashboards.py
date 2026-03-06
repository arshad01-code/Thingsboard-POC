from fastapi import APIRouter
from services.tb_client import ThingsBoardClient

router = APIRouter()

tb = ThingsBoardClient()

@router.post("/dashboards")
def create_dashboard(name: str):
    return tb.create_dashboard(name)