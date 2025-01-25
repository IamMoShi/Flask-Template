import os

from flask import Flask

from flask_app.extensions.database import db as flask_database


def create_app():
    app = Flask(__name__)
    return app
