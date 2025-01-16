from flask_app.config.general import General


class TestConfig(General):
    """
    Define global behavior for testing environment.
    Environment for running tests should be isolated from the production environment
    """
    TESTING = True
    DB_SERVER = "localhost"


class UnitTestConfig(TestConfig):
    """
    Define global behavior for unit testing environment.
    This configuration is based on the Test configuration
    """
    # In-memory database
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class IntegrationTestConfig(TestConfig):
    # Database file
    SQLALCHEMY_DATABASE_URI = "sqlite:///Tests/database/test.db"
