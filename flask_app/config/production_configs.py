from flask_app.config.general import General


class ProductionConfig(General):
    """
    Define global behavior for production environment
    """
    pass


class ProductionConfigSQLite(ProductionConfig):
    """
    Exemple of concrete configuration for production environment
    This configuration uses SQLite database
    """
    # Database file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'
