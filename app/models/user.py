import re
import string
import uuid

from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from app.constants import (
    EMAIL_MAX_LENGTH,
    PASSWORD_CHARS,
    PASSWORD_HASH_LENGTH,
    PASSWORD_MAX_LENGTH,
    PASSWORD_MIN_LENGTH,
    SPECIAL_CHARS,
    USERNAME_MAX_LENGTH,
    USERNAME_MIN_LENGTH,
    UUID_LENGTH,
)
from app.errors.data_error import (
    EmailValidationError,
    PasswordError,
    UsernameValidationError,
)
from app.errors.error_codes import data_errors
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
                message=(
                    f"Username must be at least "
                    f"{USERNAME_MIN_LENGTH} characters long"
                ),
                code=data_errors["00001"],
            )

        if len(value) > USERNAME_MAX_LENGTH:
            raise UsernameValidationError(
                message=(
                    f"Username must be at most "
                    f"{USERNAME_MAX_LENGTH} characters long"
                ),
                code=data_errors["00002"],
            )

        if not re.match(r"^[\w_]+$", value):
            raise UsernameValidationError(
                message=(
                    f"Username contains invalid characters. "
                    f"Allowed characters: {PASSWORD_CHARS}"
                ),
                code=data_errors["00003"],
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
            raise EmailValidationError(
                message="Email is too long.",
                code=data_errors["00002"],
            )

        allowed_chars = string.ascii_letters + string.digits + "@._-"
        if any(char not in allowed_chars for char in value):
            raise EmailValidationError(
                message="Email contains invalid characters.",
                code=data_errors["00003"],
            )

        if not re.match(r"^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$", value):
            raise EmailValidationError(
                message="Invalid email format.",
                code=data_errors["00005"],
            )

    # ---------- Password ----------
    @property
    def password(self):
        """Returns the password of the user."""
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, raw_password):
        """Sets the password of the user."""
        self.validate_password_strength(raw_password)
        self._password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        """Checks the password of the user."""
        return check_password_hash(self._password_hash, raw_password)

    def validate_password_strength(self, password):
        """Check if the password respects the password strength."""
        if len(password) < PASSWORD_MIN_LENGTH:
            raise PasswordError(
                message=f"Password must be at least "
                f"{PASSWORD_MIN_LENGTH} characters long",
                code=data_errors["00001"],
            )

        if len(password) > PASSWORD_MAX_LENGTH:
            raise PasswordError(
                message=f"Password must be at most"
                f" {PASSWORD_MAX_LENGTH} characters long",
                code=data_errors["00002"],
            )

        if not any(letter in SPECIAL_CHARS for letter in password):
            raise PasswordError(
                message=f"Password must contain at least one "
                f"special character. "
                f"Allowed: {SPECIAL_CHARS}",
                code=data_errors["00005"],
            )

        if any(letter not in PASSWORD_CHARS for letter in password):
            raise PasswordError(
                message=f"Password contains invalid characters. "
                f"Allowed: {PASSWORD_CHARS}",
                code=data_errors["00003"],
            )

    def change_password(self, old_password, new_password):
        """Changes the password of the user."""
        if not self.check_password(old_password):
            raise PasswordError(
                message="Current password is incorrect.",
                code=data_errors["00004"],
            )
        self.validate_password_strength(new_password)
        self.password = new_password
