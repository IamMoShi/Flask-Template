import traceback

from flask import jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from app.errors.data_error import (
    EmailValidationError,
    PasswordError,
    UsernameValidationError,
)


def register_error_handlers(app):
    """Register error handlers.

    You can register your own error handlers here. So you don't need to
    add try catch everywhere, the flask server will directly send the
    error to the client with corresponding answer and code.
    """

    @app.errorhandler(UsernameValidationError)
    def handle_username_error(error):
        return (
            jsonify(
                {
                    "error": "USERNAME_ERROR",
                    "message": error.message,
                    "code": error.code,
                }
            ),
            400,
        )

    @app.errorhandler(PasswordError)
    def handle_password_error(error):
        return (
            jsonify(
                {
                    "error": "PASSWORD_ERROR",
                    "message": error.message,
                    "code": error.code,
                }
            ),
            400,
        )

    @app.errorhandler(EmailValidationError)
    def handle_email_error(error):
        return (
            jsonify(
                {
                    "error": "EMAIL_ERROR",
                    "message": error.message,
                    "code": error.code,
                }
            ),
            400,
        )

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return (
            jsonify(
                {
                    "error": "VALIDATION_FAILED",
                    "message": "Validation failed.",
                    "fields": error.messages,
                    "code": "VALIDATION_FAILED",
                }
            ),
            422,
        )

    # Global fallback
    # pylint: disable=unused-argument
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        if isinstance(error, HTTPException):
            # Let Flask Manage HTTP errors normally (404, 403, etc.)
            return error

        # Log trace
        app.logger.error(f"Unhandled Exception: {error}")
        app.logger.error(traceback.format_exc())

        return (
            jsonify(
                {
                    "error": "SERVER_ERROR",
                    "message": "An internal error occurred.",
                    "code": "INTERNAL_ERROR",
                }
            ),
            500,
        )
