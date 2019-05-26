import jwt
from sanic.request import Request
from core.exceptions import TokenHeaderException, DecodeErrorException, InvalidTokenException
from core.config import JWT_SECRET_KEY, JWT_ALGORITHM


class TokenHelper:
    @classmethod
    def extract_from_request(cls, request: Request):
        try:
            return request.headers.get('Authorization').split('Bearer ')[1]
        except (IndexError, AttributeError):
            raise TokenHeaderException

    @classmethod
    def decode(cls, token: str) -> dict:
        try:
            return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        except jwt.exceptions.DecodeError:
            raise DecodeErrorException
        except jwt.exceptions.InvalidTokenError:
            raise InvalidTokenException

    @classmethod
    def encode(cls, user_id: int):
        return jwt.encode(payload={'user_id': user_id}, key=JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
