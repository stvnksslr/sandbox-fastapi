from fastapi import APIRouter
from typing import List

from src.models.database.Users import Users, User_Pydantic, UserIn_Pydantic

# router setting
user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@user_router.post("/")
async def create_user(request: UserIn_Pydantic):
    """
    Api endpoint to create users
    """
    user = await Users.create(**request.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user)


@user_router.get("/", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(Users.all())
