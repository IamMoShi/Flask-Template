import logging.config
import os

from flask import Flask

from flask_app.config import DevelopmentConfig as DevConfig
from flask_app import create_app
from flask_app import flask_database as db


def dev() -> Flask:
    """
    This function is used to create the app in development mode.
    :return: The flask app configured for development.
    """
    flask_app: Flask = create_app()
    with flask_app.app_context():
        # Load the configuration for the app (class -to-> app.config[keys])
        flask_app.config.from_object(DevConfig)

        os.makedirs(flask_app.config["LOGGING_DIRECTORY"], exist_ok=True)
        # Load the logging configuration from the logging configuration file
        logging.config.fileConfig(flask_app.config["LOGGING_CONFIGURATION_FILE"])

        # Blueprints to be loaded in the app - change this to the routes you want to load in the app.
        # Blueprints needs app environment because they use app logger to log the loading of the blueprint.
        from flask_app.routes.custom_bp import DevelopmentBlueprint, ProductionBlueprint

        DevelopmentBlueprint.load_all(flask_app)
        ProductionBlueprint.load_all(flask_app)

        # Plugins must be loaded before the database is initialized.
        # The plugins will load the models used in this specific configuration of the app.
        db.init_app(flask_app)
        db.create_all()
        flask_app.logger.info(f"Database initialized")

    return flask_app


if __name__ == "__main__":
    app: Flask = dev()
    app.run(host=app.config["FLASK_RUN_HOST"], port=app.config["FLASK_RUN_PORT"], debug=app.config["DEBUG"])
