from flask import Blueprint, jsonify, request
from flask_babel import gettext

from app.schemas.user_schema import UserSchema
from app.services.user_service import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)

user_bp = Blueprint("user", __name__, url_prefix="/api/users")
user_schema = UserSchema()


@user_bp.post("/register")
def register_user():
    """
    Register a new user.
    """
    data = user_schema.load(request.get_json())

    if get_user_by_username(data["username"]):
        return jsonify({"message": gettext("Username already exists")}), 409

    if get_user_by_email(data["email"]):
        return jsonify({"message": gettext("Email already taken")}), 409

    user = create_user(
        username=data["username"],
        password=data["password"],
        email=data["email"],
    )

    return user_schema.dump(user), 201
