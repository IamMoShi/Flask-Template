import os


# pylint: disable=too-few-public-methods
class FlaskConfig:
    """Configuration of flask app The configuration mainly work with
    environment variables.

    But to be easier to use for development, default values are set.
    """

    SECRET_KEY: str = os.environ.get("SECRET_KEY", "dev")

    TESTING = os.environ.get("TESTING", "False").lower() in [
        "1",
        "true",
        "yes",
    ]

    DEBUG = os.environ.get("DEBUG", "True").lower() in ["1", "true", "yes"]

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///database.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret")
