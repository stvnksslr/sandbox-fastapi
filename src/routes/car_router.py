from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

from src.models.database.Cars import Cars

# router setting
car_router = APIRouter(
    prefix="/cars",
    tags=["cars"],
    responses={404: {"description": "Not found"}},
)


class CarModel(BaseModel):
    user_id: int = 1
    manufacturer: str = "nissan"
    model: str = "altima"


@car_router.post("/")
async def create_car(request: CarModel):
    """
    Api endpoint to create cars
    """
    car = await Cars.create(**request.dict(exclude_unset=True))
    return await car


@car_router.get("/")
async def get_cars():
    return await Cars.all()
