import logging.config
import os

from flask import Flask

from flask_app.config import DevelopmentConfig as DevConfig
from flask_app import create_app
from flask_app import flask_database as db


def dev() -> Flask:
    app = create_app()
    with app.app_context():
        # Load the configuration for the app (class -to-> app.config[keys])
        app.config.from_object(DevConfig)

        os.makedirs(app.config["LOGGING_DIRECTORY"], exist_ok=True)
        # Load the logging configuration from the logging configuration file
        logging.config.fileConfig(app.config["LOGGING_CONFIGURATION_FILE"])

        # Blueprints to be loaded in the app - change this to the routes you want to load in the app.
        # Blueprints needs app environment because they use app logger to log the loading of the blueprint.
        from flask_app.routes.CustomBP import DevelopmentBlueprint, ProductionBlueprint

        DevelopmentBlueprint.load_all(app)
        ProductionBlueprint.load_all(app)

        # Plugins must be loaded before the database is initialized.
        # The plugins will load the models used in this specific configuration of the app.
        db.init_app(app)
        db.create_all()
        app.logger.info("Database initialized")

    return app


if __name__ == "__main__":
    app: Flask = dev()
    print(app.config["FLASK_RUN_HOST"])
    app.run(host=app.config["FLASK_RUN_HOST"], port=app.config["FLASK_RUN_PORT"], debug=app.config["DEBUG"])
