from marshmallow import Schema, pre_load
from core.exceptions import UnknownFieldException


class BaseSchema(Schema):
    @pre_load
    def validate_unknown_fields(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise UnknownFieldException
