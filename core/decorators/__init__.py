import jwt
from functools import wraps
from core.config import JWT_SECRET_KEY, JWT_ALGORITHM
from core.exceptions import TokenHeaderException, DecodeErrorException, InvalidTokenException


def is_jwt_authenticated(function):
    @wraps(function)
    def authenticate(request, user_id: int = None):
        try:
            token = request.headers.get('Authorization').split('Bearer ')[1]
        except (IndexError, AttributeError):
            raise TokenHeaderException

        try:
            jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            result = function(request, user_id)
            return result
        except jwt.exceptions.DecodeError:
            raise DecodeErrorException
        except jwt.exceptions.InvalidTokenError:
            raise InvalidTokenException
    return authenticate
