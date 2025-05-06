class UsernameValidationError(Exception):
    """Raised when a username is invalid."""

    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code


class PasswordError(Exception):
    """Raised when an invalid password is entered."""

    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code


class EmailValidationError(Exception):
    """Raised when an invalid email is entered."""

    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code
