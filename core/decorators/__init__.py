import jwt
from functools import wraps
from core.config import JWT_SECRET_KEY, JWT_ALGORITHM
from core.exceptions import TokenHeaderException, DecodeErrorException, InvalidTokenException


def is_jwt_authenticated():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            try:
                token = request.headers.get('Authorization').split('Bearer ')[1]
            except (IndexError, AttributeError):
                raise TokenHeaderException

            try:
                jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
                response = await f(request, *args, **kwargs)
                return response
            except jwt.exceptions.DecodeError:
                raise DecodeErrorException
            except jwt.exceptions.InvalidTokenError:
                raise InvalidTokenException
        return decorated_function
    return decorator
