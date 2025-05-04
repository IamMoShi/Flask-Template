import re
import string
import uuid

from flask_babel import gettext
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from app.constants import (
    EMAIL_MAX_LENGTH,
    PASSWORD_HASH_LENGTH,
    PASSWORD_MAX_LENGTH,
    PASSWORD_MIN_LENGTH,
    PASSWORD_SPECIFIC_CHARS,
    USERNAME_MAX_LENGTH,
    USERNAME_MIN_LENGTH,
    UUID_LENGTH,
)
from app.errors.data_error import (
    EmailValidationError,
    PasswordError,
    UsernameValidationError,
)
from app.extensions import db
from app.models.mixins.timestamp_mixins import TimestampMixin


class User(db.Model, TimestampMixin):
    """Database model for users.

    The data validation is also done in this class.
    """

    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(
        db.String(UUID_LENGTH),
        unique=True,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    _username: Mapped[str] = mapped_column(
        "username", db.String(USERNAME_MAX_LENGTH), unique=True, nullable=False
    )

    _email: Mapped[str] = mapped_column(
        "email", db.String(EMAIL_MAX_LENGTH), unique=True, nullable=False
    )

    _password_hash: Mapped[str] = mapped_column(
        "password_hash",
        db.String(PASSWORD_HASH_LENGTH),
        nullable=False,
    )

    # ---------- Username ----------
    @property
    def username(self):
        """Returns the username of the user."""
        return self._username

    @username.setter
    def username(self, value: str):
        """Sets the username of the user."""
        value = value.strip().lower()
        self._validate_username(value)
        self._username = value

    def _validate_username(self, value: str):
        """Validates that the username ensure defined constraints."""
        if len(value) < USERNAME_MIN_LENGTH:
            raise UsernameValidationError(
                gettext(
                    "Username must be at least %(num)s characters long",
                    USERNAME_MIN_LENGTH,
                )
            )

        if len(value) > USERNAME_MAX_LENGTH:
            raise UsernameValidationError(
                gettext(
                    "Username is too long. "
                    "Username must be at most %(num)s characters long",
                    USERNAME_MAX_LENGTH,
                )
            )

        if " " in value:
            raise UsernameValidationError(
                gettext(
                    "Username must not contain spaces.",
                    PASSWORD_SPECIFIC_CHARS,
                )
            )

        if not re.match(r"^[\w_]+$", value):
            raise UsernameValidationError(
                gettext(
                    "Username contains invalid characters. "
                    "Allowed characters: %(char)s",
                    PASSWORD_SPECIFIC_CHARS,
                )
            )

    # ---------- Email ----------
    @property
    def email(self):
        """Returns the email of the user."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Sets the email of the user."""
        value = value.strip().lower()
        self._validate_email(value)
        self._email = value

    def _validate_email(self, value: str):
        """Validates that the email ensure defined constraints."""

        if len(value) > EMAIL_MAX_LENGTH:
            raise EmailValidationError(gettext("Email is too long."))

        allowed_chars = string.ascii_letters + string.digits + "@._-"
        if any(char not in allowed_chars for char in value):
            raise EmailValidationError(
                gettext("Email contains invalid characters.")
            )

        if not re.match(r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$", value):
            raise EmailValidationError(gettext("Invalid email format."))

    # ---------- Password ----------
    @property
    def password(self):
        """Returns the password of the user."""
        raise AttributeError(gettext("Password is write-only."))

    @password.setter
    def password(self, raw_password):
        """Sets the password of the user."""
        self._password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        """Checks the password of the user."""
        return check_password_hash(self._password_hash, raw_password)

    def password_strong(self, password):
        """Check if the password respects the password strength."""
        if len(password) < PASSWORD_MIN_LENGTH:
            raise PasswordError(
                gettext(
                    "Password must be at least %(num)s characters long",
                    PASSWORD_MIN_LENGTH,
                )
            )

        if len(password) > PASSWORD_MAX_LENGTH:
            raise PasswordError(
                gettext(
                    "Password must be at most %(num)s characters long",
                    PASSWORD_MAX_LENGTH,
                )
            )

        if any(letter not in PASSWORD_SPECIFIC_CHARS for letter in password):
            raise PasswordError(
                gettext(
                    "Password contains invalid characters. "
                    "Password can only contain: %(char)s",
                    PASSWORD_SPECIFIC_CHARS,
                )
            )

    def change_password(self, old_password, new_password):
        """Changes the password of the user."""
        if not self.check_password(old_password):
            raise PasswordError(
                gettext(
                    "Current password is incorrect.",
                )
            )

        self.password = new_password
