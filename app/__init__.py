import time

from flask import Flask
from sqlalchemy.exc import OperationalError

from app.config.flask_config import FlaskConfig
from app.errors.error_handlers import register_error_handlers
from app.extensions import db, jwt, migrate
from app.routes import register_routes


def wait_for_db(app, max_retries=10, delay=2):
    """This function will wait until the database is available or if it reached
    max retries."""
    for i in range(max_retries):
        try:
            with app.app_context():
                db.create_all()
            return
        except OperationalError:
            app.logger.warning(
                f"Database not ready. Retry {i + 1}/{max_retries}..."
            )
            time.sleep(delay)
    raise RuntimeError("Database not available after retries")


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

    return app
