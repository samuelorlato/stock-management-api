from flask import jsonify, Response
from src.domain.errors.errors import CustomError

class ApiErrorHandling:
    @staticmethod
    def handle_error(error: CustomError) -> Response:
        response = jsonify(
            {
                "error_description": error.description, 
                "error": str(error.original_exception)
            }
        )
        response.status_code = error.code

        return response