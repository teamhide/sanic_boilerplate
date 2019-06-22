from core.schemas import BaseSchema
from marshmallow import fields


# Request Serializer
class CreateUserRequestSchema(BaseSchema):
    email = fields.Email(required=True)
    password1 = fields.Str(required=True)
    password2 = fields.Str()
    nickname = fields.Str(required=True)
    gender = fields.Str(required=True)
    join_type = fields.Str(required=True)


class UpdateUserRequestSchema(BaseSchema):
    password = fields.Str(required=True)
    target_field = fields.Str(required=True)
    value = fields.Str(required=True)


class LoginRequestSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    join_type = fields.Str(required=True)


# Response Serializer
class UserResponseSchema(BaseSchema):
    email = fields.Email()
    nickname = fields.Str()
    gender = fields.Str()


class LoginResponseSchema(BaseSchema):
    token = fields.Str()
