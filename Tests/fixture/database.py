import pytest
from flask_app.extensions.database import database as db


@pytest.fixture(autouse=True)
def clean_db():
    connection = db.engine.connect()
    transaction = connection.begin()

    db.session.bind = connection
    db.session.begin_nested()

    yield  # Test execution

    db.session.rollback()
    transaction.rollback()
    connection.close()
