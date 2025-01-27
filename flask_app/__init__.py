import os

from flask import Flask

# database is import to facilitate calling the db in the project
from flask_app.extensions.database import db as flask_database


def create_app() -> Flask:
    """
    Create a Flask app without any configuration
    :return: flask app
    """
    app: Flask = Flask(__name__)
    return app
