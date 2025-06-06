from fastapi import APIRouter

import app.utils as utils
from app.models.configurations import Settings

router = APIRouter()


@router.get("/info")
async def info():
    settings: Settings = utils.get_settings()
    return {"app_name": settings.app_name, "debug_mode": settings.debug}
