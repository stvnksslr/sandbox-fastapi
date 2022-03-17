from tortoise import fields
from tortoise.models import Model


class Cars(Model):
    id = fields.IntField(pk=True)
    manufacturer = fields.TextField()
    model = fields.TextField()
    user = fields.ForeignKeyField("models.Users", related_name="cars")
    created_at = fields.DatetimeField(null=True, auto_now=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        table = "car"


