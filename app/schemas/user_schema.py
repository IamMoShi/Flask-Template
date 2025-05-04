from marshmallow import Schema, fields, validate

from app.constants import PASSWORD_MIN_LENGTH, USERNAME_MAX_LENGTH


class UserSchema(Schema):
    """Represents user schema, that's the structure of json use to discuss user
    models."""

    uuid = fields.Str(
        dump_only=True
    )  # Corresponds to the `uuid` field (in reading alone)

    username = fields.Str(
        required=True, validate=validate.Length(max=USERNAME_MAX_LENGTH)
    )

    email = fields.Email(
        required=True,
    )

    password = fields.Str(
        required=True,
        load_only=True,
        validate=validate.Length(min=PASSWORD_MIN_LENGTH),
    )

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
