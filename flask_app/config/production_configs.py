import os

from flask_app.config.general import General


class ProductionConfig(General):
    """
    Define global behavior for production environment
    """
    PORT = os.environ.get("PORT", 5000)  # Default port is 5000
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///production.db")
