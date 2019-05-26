from functools import wraps


def is_jwt_authenticated(function):
    @wraps(function)
    def measure(*args, **kwargs):
        result = function(*args, **kwargs)
        return result
    return measure
