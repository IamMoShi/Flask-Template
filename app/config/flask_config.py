import os


# pylint: disable=too-few-public-methods
class FlaskConfig:
    """Configuration for the Flask application.

    Most values are pulled from environment variables, with default
    values provided to simplify local development.
    """

    # Secret key for session management and CSRF protection
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "dev")

    # Enables testing mode if TESTING is set to 1/true/yes
    TESTING = os.environ.get("TESTING", "False").lower() in [
        "1",
        "true",
        "yes",
    ]

    # Enables debug mode if DEBUG is set to 1/true/yes
    DEBUG = os.environ.get("DEBUG", "True").lower() in ["1", "true", "yes"]

    # SQLAlchemy database URI (default is a local SQLite file)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///database.db"
    )

    # Disables SQLAlchemy event system to improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key used to sign JWT tokens
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret")

    # Directory path where application logs will be stored
    LOG_DIR = os.environ.get("LOG_DIR", "logs")

    # Set of authorized IP addresses allowed to access the /metrics endpoint
    # Reads from the AUTHORIZED_PROMETHEUS_IPS environment variable,
    # comma-separated
    AUTHORIZED_METRICS_IPS = set(
        ip.strip()
        for ip in os.environ.get("AUTHORIZED_METRICS_IPS", "172.20.0.5").split(
            ","
        )
    )
