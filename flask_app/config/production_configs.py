import os

from flask_app.config.general import General


class ProductionConfig(General):
    """
        For production
    """
    """
    ################################################################
    FLASK CONFIGURATION
    ################################################################
    """

    DEBUG = False

    """
    ################################################################
    LOGGING CONFIGURATION
    ################################################################
    """

    LOGGING_LEVEL = "info"

    """
    ################################################################
    DATABASE CONFIGURATION
    ################################################################
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
