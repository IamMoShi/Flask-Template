from flask import jsonify
from marshmallow import ValidationError

from app.errors.data_error import UsernameValidationError, PasswordChangeError, EmailValidationError


def register_error_handlers(app):
    @app.errorhandler(UsernameValidationError)
    def handle_username_error(error):
        message = error.code
        return jsonify({
            "error": "USERNAME_ERROR",
            "message": message,
            "code": error.code
        }), 400

    @app.errorhandler(PasswordChangeError)
    def handle_password_error(error):
        message = error.code
        return jsonify({
            "error": "PASSWORD_ERROR",
            "message": message,
            "code": error.code
        }), 400

    @app.errorhandler(EmailValidationError)
    def handle_email_error(error):
        message = error.code
        return jsonify({
            "error": "EMAIL_ERROR",
            "message": message,
            "code": error.code
        }), 400

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({
            "error": "VALIDATION_FAILED",
            "message": "Validation failed.",
            "fields": error.messages,
            "code": "VALIDATION_FAILED"
        }), 422

    # Global fallback
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        import traceback
        print("UNHANDLED EXCEPTION:\n", traceback.format_exc())

        return jsonify({
            "error": "SERVER_ERROR",
            "message": "An internal error occurred.",
            "code": "INTERNAL_ERROR"
        }), 500
