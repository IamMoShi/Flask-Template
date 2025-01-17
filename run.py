from flask_app import create_app
from flask_app.extensions.database import database

# Import the config that you want to use in run.py file. Do not modify as RunConfig.
from flask_app.config import DevelopmentConfigSQLite as RunConfig

# Setup logging for the app
from flask_app.logs import setup_logging

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        app.config.from_object(RunConfig)
        setup_logging(app)

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

        app.run()
