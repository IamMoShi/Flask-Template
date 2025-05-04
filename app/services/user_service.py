import uuid

from app import db
from app.models.user import User


def get_user_by_username(username: str) -> User | None:
    return User.query.filter_by(_username=username.lower().strip()).first()


def get_user_by_email(email: str) -> User | None:
    return User.query.filter_by(_email=email.lower().strip()).first()


def get_user_by_id(user_id: int) -> User | None:
    return User.query.get(user_id)


def create_user(username: str, email: str, password: str) -> User:

    user = User()

    user.username = username
    user.email = email
    user.password = password

    db.session.add(user)
    db.session.commit()
    return user
