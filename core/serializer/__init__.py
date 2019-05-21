from marshmallow import Schema, pre_load


class BaseSchema(Schema):
    @pre_load
    def validate(self, data):
        pass
