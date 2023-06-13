from fastapi import APIRouter
from pydantic import BaseModel

from src.models.database.Users import User_Response, Users

# router setting
user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


class UserRequest(BaseModel):
    email: str = "dandargan@space.com"
    first_name: str = "dan"
    last_name: str = "dargan"


@user_router.post("/")
async def create_user(request: UserRequest):
    """
    Api endpoint to create users
    """
    user = await Users.create(**request.dict(exclude_unset=True))
    return await User_Response.from_tortoise_orm(user)


@user_router.get("/")
async def get_users():
    """
    API endpoint to return all created users

    :return:
    """
    return await User_Response.from_queryset(Users.all())
