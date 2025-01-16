from flask_app import create_app
from flask_app.extensions.database import database

# Import the config that you want to use in run.py file. Do not modify as RunConfig.
from flask_app.config import DevelopmentConfigSQLite as RunConfig

# Setup logging for the app
from flask_app.logs import setup_logging

# Blueprints to be loaded in the app - change this to the blueprints you want to load in the app.
# Do not modify as RunBlueprint.
from flask_app.blueprints.CustomBP import DevelopmentBlueprint as RunBlueprint

app = create_app()

if __name__ == '__main__':
    app.config.from_object(RunConfig)
    setup_logging(app)
    database.init_app(app)

    with app.app_context():
        database.create_all()

    app.logger.info("Database initialized")

    RunBlueprint.load_all(app)
    app.logger.info("Blueprints loaded")

    app.run()
