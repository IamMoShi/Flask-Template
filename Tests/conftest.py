import os

import pytest
from flask import Flask

# Import the create_app function from the Flask application
from flask_app import create_app

# Adapt the config class to the one you are using
# Here we are using the UnitTestConfig class and the IntegrationTestConfig class
from flask_app.config.test_configs import UnitTestConfig as UnitConfig
from flask_app.config.test_configs import IntegrationTestConfig as IntegrationConfig

# Import SQLAlchemy database instance
from flask_app.extensions.database import database

from flask_app.logs import setup_logging


@pytest.fixture(scope="session")
def app():
    """Create a Flask application instance configured for testing."""

    """
    ################################################################
    Getting the test type from the environment variable
    ################################################################
    """

    test_type: str | None = os.getenv("TEST_TYPE", "unit")  # Par défaut, tests unitaires

    """
    ################################################################
    Creating the Flask application instance
    ################################################################
    """

    # Create a raw Flask application instance
    app: Flask = create_app()

    # Search the configuration class based on the test type
    app.logger.info(f"Running tests of type: {test_type}")
    if test_type == "unit":
        app.config.from_object(UnitConfig)
    elif test_type == "integration":
        app.config.from_object(IntegrationConfig)
    else:
        raise ValueError(f"Unknown test type: {test_type}")

    # Initialize the database
    app.logger.info(f"app config: {app.config}")
    app.logger.info(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    database.init_app(app)
    with app.app_context():
        database.create_all()

    # By default, the test does not use logging
    # Uncomment the following line to enable logging
    # setup_logging(app)

    # Return the application instance
    yield app
