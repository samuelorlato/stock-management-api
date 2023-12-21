from werkzeug.exceptions import HTTPException

class ValidationError(HTTPException):
    code = 400
    description = "Validation error"

class InternalError(HTTPException):
    code = 500
    description = "Internal error"