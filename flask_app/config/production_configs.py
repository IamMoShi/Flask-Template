import os

from flask_app.config.general import General


class ProductionConfig(General):
    """
    Define global behavior for production environment
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///production.db")