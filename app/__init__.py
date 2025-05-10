from flask import Flask

from app.config.flask_config import FlaskConfig
from app.errors.error_handlers import register_error_handlers
from app.extensions import db, jwt, metrics, migrate
from app.routes import register_routes
from app.services.database_services import wait_for_db


def create_app():
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)
    app.config.from_object(FlaskConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_routes(app)

    register_error_handlers(app)

    wait_for_db(app)
    metrics.init_app(app)
    return app
