from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(Model):
    id = fields.IntField(pk=True)
    email = fields.TextField()
    created_at = fields.DatetimeField(null=True, auto_now=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        table = "user"

    # class PydanticMeta:
    #     exclude = ["password"]


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)