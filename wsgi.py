from flask import Flask

from flask_app import create_app
from flask_app import flask_database as db
from flask_app.config import ProductionConfig as ProdConfig


def prod() -> Flask:
    app: Flask = create_app()
    with app.app_context():
        app.config.from_object(ProdConfig)

        app.logger.info("STARTING APP config: %s", ProdConfig.__name__)

        # Blueprints to be loaded in the app - change this to the routes you want to load in the app.
        # Blueprints needs app environment because they use app logger to log the loading of the blueprint.
        from flask_app.routes.CustomBP import ProductionBlueprint

        ProductionBlueprint.load_all(app)
        app.logger.info("Blueprints loaded")

        # Plugins must be loaded before the database is initialized.
        # The plugins will load the models used in this specific configuration of the app.
        db.init_app(app)
        db.create_all()
        app.logger.info("Database initialized")
    return app


app = prod()
