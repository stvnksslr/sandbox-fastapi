from fastapi import APIRouter

from src.routes import car_router, user_router

router = APIRouter()
router.include_router(user_router.user_router, prefix="/v1", tags=["V1"])
router.include_router(car_router.car_router, prefix="/v1", tags=["V1"])
