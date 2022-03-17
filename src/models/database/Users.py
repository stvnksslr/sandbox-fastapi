from tortoise import fields
from tortoise.models import Model


class Users(Model):
    id = fields.IntField(pk=True)
    email = fields.TextField()
    created_at = fields.DatetimeField(null=True, auto_now=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        table = "user"

    # class PydanticMeta:
    #     exclude = ["password"]
