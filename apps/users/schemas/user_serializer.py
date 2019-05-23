from core.serializer import BaseSchema
from marshmallow import fields


# Request Serializer
class CreateUserRequestSchema(BaseSchema):
    email = fields.Email()
    password1 = fields.Str()
    password2 = fields.Str()
    nickname = fields.Str()
    gender = fields.Str()
    join_type = fields.Str()


class UpdateUserRequestSchema(BaseSchema):
    password = fields.Str()
    target_field = fields.Str()
    value = fields.Str()


# Response Serializer
class UserResponseSchema(BaseSchema):
    email = fields.Email()
    nickname = fields.Str()
    gender = fields.Str()
