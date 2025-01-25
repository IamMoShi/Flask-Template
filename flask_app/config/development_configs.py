import os

from flask_app.config.general import General


class DevelopmentConfig(General):

    """
    For development
    """

    """
    ################################################################
    FLASK CONFIGURATION
    ################################################################
    """

    DEBUG = True
    FLASK_RUN_HOST = os.environ.get("FLASK_RUN_HOST", "localhost")
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT", 5000)


    """
    ################################################################
    LOGGING CONFIGURATION
    ################################################################
    """

    LOGGING_LEVEL = "debug"

    """
    ################################################################
    DATABASE CONFIGURATION
    ################################################################
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///production.db")
