from sanic.exceptions import SanicException, add_status_code


@add_status_code(404)
class NotFoundException(SanicException):
    def __init__(self):
        message = 'Not found'
        super().__init__(message)


@add_status_code(401)
class PermissionErrorException(SanicException):
    def __init__(self):
        message = 'Permission error'
        super().__init__(message)


@add_status_code(400)
class ValidationErrorException(SanicException):
    def __init__(self):
        message = 'Validation error'
        super().__init__(message)


@add_status_code(400)
class NotUniqueException(SanicException):
    def __init__(self):
        message = 'Not unique'
        super().__init__(message=message)


@add_status_code(401)
class LoginFailException(SanicException):
    def __init__(self):
        message = 'Login fail'
        super().__init__(message=message)


@add_status_code(401)
class DecodeErrorException(SanicException):
    def __init__(self):
        message = 'Token decode error'
        super().__init__(message=message)


@add_status_code(401)
class InvalidTokenException(SanicException):
    def __init__(self):
        message = 'Invalid token'
        super().__init__(message=message)


@add_status_code(401)
class TokenHeaderException(SanicException):
    def __init__(self):
        message = 'Invalid token headers'
        super().__init__(message=message)


@add_status_code(401)
class UnknownFieldException(SanicException):
    def __init__(self):
        message = 'Unknown field inside request'
        super().__init__(message=message)


@add_status_code(401)
class AlreadyExistException(SanicException):
    def __init__(self):
        message = 'Already exist'
        super().__init__(message=message)


@add_status_code(500)
class ServerErrorException(SanicException):
    def __init__(self):
        message = 'Server error'
        super().__init__(message=message)
