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
from flask_app import flask_database as db


@pytest.fixture(scope="function")
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

    # By default, the test does not use logging
    # Uncomment the following line to enable logging
    # from tests_flask_app.logs import setup_logging
    # setup_logging(app)

    # Initialize the database
    with app.app_context():
        # Blueprints to be loaded in the app - change this to the routes you want to load in the app.
        # Blueprints needs app environment because they use app logger to log the loading of the blueprint.
        from flask_app.routes.custom_bp import DevelopmentBlueprint, ProductionBlueprint
        DevelopmentBlueprint.load_all(app)
        ProductionBlueprint.load_all(app)

        db.init_app(app)
        db.create_all()

        # Return the application instance
        yield app

        db.session.remove()
        db.drop_all()
