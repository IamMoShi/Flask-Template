import re
import string
import uuid

from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from flask_babel import _

from app.errors.data_error import UsernameValidationError, PasswordChangeError, EmailValidationError
from app.extensions import db
from app.constants import UUID_LENGTH, USERNAME_MIN_LENGTH, USERNAME_MAX_LENGTH, PASSWORD_HASH_LENGTH, EMAIL_MAX_LENGTH, \
    PASSWORD_MAX_LENGTH, PASSWORD_MIN_LENGTH, PASSWORD_SPECIFIC_CHARS
from app.models.mixins.timestamp_mixins import TimestampMixin


class User(db.Model, TimestampMixin):
    uuid: Mapped[str] = mapped_column(
        db.String(UUID_LENGTH),
        unique=True,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    _username: Mapped[str] = mapped_column(
        db.String(USERNAME_MAX_LENGTH),
        unique=True,
        nullable=False
    )

    _email: Mapped[str] = mapped_column(
        db.String(EMAIL_MAX_LENGTH),
        unique=True,
        nullable=False
    )

    _password_hash: Mapped[str] = mapped_column(
        "password_hash",
        db.String(PASSWORD_HASH_LENGTH),
        nullable=False,
    )

    # ---------- Username ----------
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        value = value.strip().lower()
        self._validate_username(value)
        self._username = value

    def _validate_username(self, value: str):
        if len(value) < USERNAME_MIN_LENGTH:
            raise UsernameValidationError(
                _(f"Username must be at least {PASSWORD_MIN_LENGTH} characters long"))

        if len(value) > USERNAME_MAX_LENGTH:
            raise UsernameValidationError(
                _("Username is too long. Username must be at most %(max_length)s characters long"))

        if " " in value:
            raise UsernameValidationError(
                _("Username must not contain spaces."))

        if not re.match(r"^[\w_]+$", value):
            raise UsernameValidationError(
                _("Username contains invalid characters."))

    # ---------- Email ----------
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        value = value.strip().lower()
        self._validate_email(value)
        self._email = value

    def _validate_email(self, value: str):
        if len(value) > EMAIL_MAX_LENGTH:
            raise EmailValidationError(
                _("Email is too long."))

        allowed_chars = string.ascii_letters + string.digits + "@._-"
        if any(char not in allowed_chars for char in value):
            raise EmailValidationError(
                _("Email contains invalid characters."))

        if not re.match(r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$", value):
            raise EmailValidationError(
                _("Invalid email format."))

    # ---------- Password ----------
    @property
    def password(self):
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, raw_password):
        self._password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self._password_hash, raw_password)

    def password_strong(self, password):
        if len(password) < PASSWORD_MIN_LENGTH:
            raise (
                _("Password must be at least %(min_length)s characters long")
            )

        if len(password) > PASSWORD_MAX_LENGTH:
            raise PasswordChangeError(
                _("Password must be at most %(max_length)s characters long")
            )

        if any(letter not in PASSWORD_SPECIFIC_CHARS for letter in password):
            raise PasswordChangeError(
                _(f"Password contains invalid characters. "
                  f"Password can only contain: \n {PASSWORD_SPECIFIC_CHARS}")
            )

    def change_password(self, old_password, new_password):
        if not self.check_password(old_password):
            raise PasswordChangeError(_("Current password is incorrect."))

        self.password = new_password
