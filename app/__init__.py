from flask import Flask, request

from app.config.flask_config import FlaskConfig
from app.errors.error_handlers import register_error_handlers
from app.extensions import babel, db, jwt, migrate
from app.routes import register_routes


def select_locale():
    """Determine which locale to use (for babel translation)."""
    return request.accept_languages.best_match(["en", "fr"])


def create_app():
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)
    app.config.from_object(FlaskConfig)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    migrate.init_app(app, db)
    jwt.init_app(app)
    babel.init_app(app, locale_selector=select_locale)

    register_routes(app)
    register_error_handlers(app)

    return app
