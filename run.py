from flask_app import create_app
from flask_app.extensions.database import database

# Import the config that you want to use in run.py file. Do not modify as RunConfig.
from flask_app.config import DevelopmentConfigSQLite as DevConfig
from flask_app.config import ProductionConfigSQLite as ProdConfig

# Setup logging for the app
from flask_app.logs import setup_logging


def dev():
    app = create_app()
    with app.app_context():
        app.config.from_object(DevConfig)
        setup_logging(app)
        app.logger.info("STARTING APP config: %s", DevConfig.__name__)

        # Blueprints to be loaded in the app - change this to the blueprints you want to load in the app.
        # Blueprints needs app environment because they use app logger to log the loading of the blueprint.
        from flask_app.blueprints.CustomBP import DevelopmentBlueprint, ProductionBlueprint

        DevelopmentBlueprint.load_all(app)
        ProductionBlueprint.load_all(app)
        app.logger.info("Blueprints loaded")

        # Plugins must be loaded before the database is initialized.
        # The plugins will load the models used in this specific configuration of the app.
        database.init_app(app)
        database.create_all()
        app.logger.info("Database initialized")

        app.run(host="0.0.0.0", port=DevConfig.PORT)


def prod():
    app = create_app()
    with app.app_context():
        app.config.from_object(ProdConfig)
        setup_logging(app)
        app.logger.info("STARTING APP config: %s", ProdConfig.__name__)

        # Blueprints to be loaded in the app - change this to the blueprints you want to load in the app.
        # Blueprints needs app environment because they use app logger to log the loading of the blueprint.
        from flask_app.blueprints.CustomBP import ProductionBlueprint

        ProductionBlueprint.load_all(app)
        app.logger.info("Blueprints loaded")

        # Plugins must be loaded before the database is initialized.
        # The plugins will load the models used in this specific configuration of the app.
        database.init_app(app)
        database.create_all()
        app.logger.info("Database initialized")
        app.logger.info("Running app on port %s", ProdConfig.PORT)
        app.run(host="0.0.0.0", port=ProdConfig.PORT)


if __name__ == "__main__":
    # Check in the environment variable to see if the app is running in production or development.
    # If the environment variable is not set, the app will run in development mode.
    import os
    if os.environ.get("FLASK_ENV") == "production":
        prod()
    else:
        dev()
