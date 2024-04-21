from ninja import ModelSchema
from login.models import User
from ninja import Schema

class UserSchema(ModelSchema):
    class Config:
        model=User
        model_fields = ['password','username','last_login']

class UserProfileSchema(ModelSchema):
    class Config:
        model=User
        model_fields = ['username']

class TokenSchema(Schema):
    token:str

class UserLoginSchema(Schema):
    username:str
    password:str