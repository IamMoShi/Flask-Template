class UsernameValidationError(Exception):
    def __init__(self, code: str):
        self.message = code


class PasswordChangeError(Exception):
    def __init__(self, code: str):
        self.code = code


class EmailValidationError(Exception):
    def __init__(self, code: str):
        self.code = code
