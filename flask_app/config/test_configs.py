from flask_app.config.general import General


class TestConfig(General):
    """
    Define global behavior for testing environment.
    Environment for running tests should be isolated from the production environment
    """
    TESTING = True
    # In-memory database
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class UnitTestConfig(TestConfig):
    """
    Define global behavior for unit testing environment.
    This configuration is based on the Test configuration
    """

    # SQLALCHEMY_DATABASE_URI = "sqlite:///unit.db"
    SQLALCHEMY_DATABASE_URI = "mysql://user:user_password@localhost:3307/my_database"


class IntegrationTestConfig(TestConfig):
    # Database file
    SQLALCHEMY_DATABASE_URI = "sqlite:///integration.db"
