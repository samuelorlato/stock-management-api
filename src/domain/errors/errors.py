from werkzeug.exceptions import HTTPException

class CustomError(HTTPException):
    def __init__(self, message, original_exception=None):
        super().__init__(description=message)
        self.original_exception = original_exception

class ValidationError(CustomError):
    code = 400

class InternalError(CustomError):
    code = 500