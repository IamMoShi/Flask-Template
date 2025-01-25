from flask import render_template

from flask_app.routes.CustomBP.ProductionBlueprints import ProductionBlueprint as MyBlueprint
from flask_app.models import ExampleModel
from flask_app import flask_database as db

"""
################################################################
Define a blueprint type production.
A blueprint is a way to organize related group routes in a 
Flask application.
It is a way to separate concerns and make the code more modular.

url_prefix: The prefix that will be added to all routes in this 
blueprint.
example: if url_prefix='/bp1', then the route '/' will be 
'/bp1/'.

!!! The blueprint needs to be add to __init__.py to be loaded 
by the application.
################################################################
"""
bp_example_prod_1 = MyBlueprint('bp_example_prod_1', __name__, url_prefix='/bp1')

"""
################################################################
This is a route in the blueprint.
A route is a way to define a URL that will be handled by the 
application.
################################################################
"""


@bp_example_prod_1.route('/')
def index():
    return 'Hello, bp1!'


@bp_example_prod_1.route("/test")
def test():
    return "Test bp1"


@bp_example_prod_1.route("/template")
def template():
    return render_template('bp1/index.html')


@bp_example_prod_1.route("/model")
def model():
    my_model: ExampleModel = ExampleModel(name="bp1")
    db.session.add(my_model)
    db.session.commit()
    return f"{my_model.id}"
