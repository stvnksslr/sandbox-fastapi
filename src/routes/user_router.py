from fastapi import APIRouter
from pydantic import BaseModel

from src.models.database.Users import Users

# router setting
user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


class UserRequest(BaseModel):
    email: str


@user_router.post("/")
async def create_user(request: UserRequest):
    """
    Api endpoint to create users
    """
    user = await Users.create(**request.dict(exclude_unset=True))
    return await user


@user_router.get("/")
async def get_users():
    return await Users.all()
