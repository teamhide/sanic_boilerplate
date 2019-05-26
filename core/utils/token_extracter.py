from sanic.request import Request
from core.exceptions import TokenHeaderException


class TokenExtractor:
    def __init__(self, request: Request):
        try:
            self.header = request.headers.get('Authorization').split('Bearer ')[1]
        except (IndexError, AttributeError):
            raise TokenHeaderException

    def extract(self):
        return self.header
