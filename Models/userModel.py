
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    email = fields.CharField(max_length=200)
    password = fields.CharField(max_length=200)
    def __str__(self):
        return self.name


User_Pydantic = pydantic_model_creator(Users, name="Users")     
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn")    