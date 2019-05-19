from marshmallow import Schema, fields


# Request Serializer
class UserRequestSerializer(Schema):
    email = fields.Email()
    password = fields.Str()
    nickname = fields.Str()
    gender = fields.Str()
    is_active = fields.Boolean()
    is_block = fields.Boolean()


# Response Serializer
class UserResponseSerializer(Schema):
    email = fields.Email()
    nickname = fields.Str()
    gender = fields.Str()
