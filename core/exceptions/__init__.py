from sanic.exceptions import SanicException, add_status_code


@add_status_code(404)
class NotFoundException(SanicException):
    def __init__(self):
        message = 'Not found exception'
        super().__init__(message)


@add_status_code(401)
class DoNotHavePermissionException(SanicException):
    def __init__(self):
        message = 'Do not have permission'
        super().__init__(message)


@add_status_code(400)
class ValidationErrorException(SanicException):
    def __init__(self):
        message = 'Validation error exception'
        super().__init__(message)


@add_status_code(400)
class NotUniqueException(SanicException):
    def __init__(self):
        message = 'Not unique exception'
        super().__init__(message=message)
