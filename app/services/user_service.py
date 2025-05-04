from app import db
from app.models.user import User


def get_user_by_username(username: str) -> User | None:
    """
    Get user by username
    """
    return User.query.filter_by(_username=username.lower().strip()).first()


def get_user_by_email(email: str) -> User | None:
    """
    Get user by email
    """
    return User.query.filter_by(_email=email.lower().strip()).first()


def get_user_by_id(user_id: int) -> User | None:
    """
    Get user by uuid
    """
    return User.query.get(user_id)


def create_user(username: str, email: str, password: str) -> User:
    """
    Create new user
    This function does not check if the user is already registered
    or if the data are incorrect.
    Checking duplication must be performed before creating a new user.
    The database will block bad data, but check can be performed before too.
    """

    user = User()

    user.username = username
    user.email = email
    user.password = password

    db.session.add(user)
    db.session.commit()
    return user
