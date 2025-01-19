from flask import Flask

from flask_app.models import ExampleModel
from flask_app.extensions.database import database as db


class TestUnitExampleModel:
    def test_create(self, app: Flask):
        with app.app_context():
            assert ExampleModel.query.count() == 0
            my_model: ExampleModel = ExampleModel(name="name1", description="d1")

            db.session.add(my_model)
            db.session.commit()
            assert my_model.id is not None  # Vérifiez que l'id a bien été généré
            assert ExampleModel.query.count() == 1

    def test_create2(self, app: Flask):
        with app.app_context():
            assert ExampleModel.query.count() == 0
            my_model: ExampleModel = ExampleModel(name="name1", description="d1")

            db.session.add(my_model)
            db.session.commit()
            assert my_model.id is not None  # Vérifiez que l'id a bien été généré
            assert ExampleModel.query.count() == 1
