from flask import Flask

from flask_app.extensions.database import database


def create_app():
    app = Flask(__name__)
    return app
