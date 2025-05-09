import logging
import os
import time
from logging.handlers import RotatingFileHandler

from flask import Flask, Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    CollectorRegistry,
    generate_latest,
    multiprocess,
)
from sqlalchemy.exc import OperationalError

from app.config.flask_config import FlaskConfig
from app.errors.error_handlers import register_error_handlers
from app.extensions import db, jwt, metrics, migrate
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


def configure_logging(app):
    """Configure logging for the Flask application."""
    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=10_000_000, backupCount=5
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: "
            "%(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    file_handler.setLevel(logging.INFO)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info("Application startup")


def create_app():
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)
    app.config.from_object(FlaskConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    register_routes(app)

    @app.route("/metrics")
    def my_metrics():
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
        data = generate_latest(registry)
        return Response(data, mimetype=CONTENT_TYPE_LATEST)

    register_error_handlers(app)

    wait_for_db(app)
    metrics.init_app(app)
    return app
