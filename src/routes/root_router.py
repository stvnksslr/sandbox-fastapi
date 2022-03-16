from fastapi import APIRouter
from src.routes.user_router import user_router

router = APIRouter()
router.include_router(user_router, prefix="/v1", tags=["V1"])
