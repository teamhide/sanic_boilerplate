from core.serializer import BaseSchema
from marshmallow import Schema, fields


# Request Serializer
class CreateUserRequestSchema(BaseSchema):
    email = fields.Email()
    password1 = fields.Str()
    password2 = fields.Str()
    nickname = fields.Str()
    gender = fields.Str()
    join_type = fields.Str()


# Response Serializer
class UserResponseSchema(BaseSchema):
    email = fields.Email()
    nickname = fields.Str()
    gender = fields.Str()
