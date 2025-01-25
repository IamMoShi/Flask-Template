from flask_app.config.general import General


class TestConfig(General):
    """
    Abstract class for test configurations
    """

    __abstract__ = True

    """
    ################################################################
    FLASK CONFIGURATION
    ################################################################
    """

    TESTING = True

    """
    ################################################################
    DATABASE CONFIGURATION
    ################################################################
    """

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class UnitTestConfig(TestConfig):
    """
        Unit test configuration
    """

    """
    ################################################################
    DATABASE CONFIGURATION
    ################################################################
    """
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class IntegrationTestConfig(TestConfig):
    """
        Integration test configuration
    """

    """
    ################################################################
    DATABASE CONFIGURATION
    ################################################################
    """

    SQLALCHEMY_DATABASE_URI = "sqlite:///integration.db"
