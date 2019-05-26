import jwt
from sanic.request import Request
from core.exceptions import TokenHeaderException, DecodeErrorException, InvalidTokenException
from core.config import JWT_SECRET_KEY, JWT_ALGORITHM


class TokenHelper:
    def __init__(self):
        pass

    def extract_from_request(self, request: Request):
        try:
            return request.headers.get('Authorization').split('Bearer ')[1]
        except (IndexError, AttributeError):
            raise TokenHeaderException

    def decode(self, token: str) -> dict:
        try:
            return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        except jwt.exceptions.DecodeError:
            raise DecodeErrorException
        except jwt.exceptions.InvalidTokenError:
            raise InvalidTokenException
