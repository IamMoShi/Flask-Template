from flask import render_template

from flask_app.blueprints.CustomBP.DevelopmentBlueprint import DevelopmentBlueprint as MyBlueprint

"""
################################################################
Define a blueprint type development.
A blueprint is a way to organize related group routes in a Flask 
application.
It is a way to separate concerns and make the code more modular.

url_prefix: The prefix that will be added to all routes in this 
blueprint.
example: if url_prefix='/bp1', then the route '/' will be 
'/bp1/'.

!!! The blueprint needs to be add to __init__.py to be loaded 
by the application.
################################################################
"""
bp_example_dev_2 = MyBlueprint('bp_example_dev_2', __name__, url_prefix='/bp2')

"""
################################################################
This is a route in the blueprint.
A route is a way to define a URL that will be handled by 
the application.
################################################################
"""


@bp_example_dev_2.route('/')
def index():
    return 'Hello, bp2!'


@bp_example_dev_2.route("/test")
def test():
    return "Test bp2"


@bp_example_dev_2.route("/template")
def template():
    return render_template('bp2/index.html')
