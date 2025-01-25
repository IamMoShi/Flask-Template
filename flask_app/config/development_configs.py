import os

from flask_app.config.general import General


class DevelopmentConfig(General):
    """
    Define global behavior for development environment
    This configuration is based on the General configuration
    """
    # Enable debug mode
    DEBUG = True


class DevelopmentConfigSQLite(DevelopmentConfig):
    """
    Exemple of concrete configuration for development environment
    This configuration uses SQLite database
    """
    # Database file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///production.db")
