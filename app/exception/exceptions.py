# Base exception Handler class
class BaseExceptions(Exception):

    def __init__(self, error: str = None, status_code: int = 400):
        self._error = error
        self._status_code = status_code

    @property
    def error(self):
        return self._error

    @property
    def status_code(self):
        return self._status_code


class UnAuthorizedException(BaseExceptions):
    pass


class ForbiddenException(BaseExceptions):
    pass


class NotFoundException(BaseExceptions):
    pass


class InternalServerError(BaseExceptions):
    pass


class BadRequestException(BaseExceptions):
    pass
