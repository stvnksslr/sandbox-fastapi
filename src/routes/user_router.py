from fastapi import APIRouter
from typing import List

from src.models.database.Users import Users
from src.models.api.Users import User_Pydantic, UserIn_Pydantic

# router setting
user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@user_router.post("/", response_model=User_Pydantic)
async def create_user(request: UserIn_Pydantic):
    """
    Api endpoint to create users
    """
    user = await Users.create(**request.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user)


@user_router.get("/")
async def get_users():
    return await User_Pydantic.from_queryset(Users.all())
