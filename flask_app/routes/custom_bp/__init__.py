from flask_app.routes.custom_bp.DevelopmentBlueprint import DevelopmentBlueprint
from flask_app.routes.custom_bp.ProductionBlueprints import ProductionBlueprint
"""
Import here the blueprint classes that you want to load in the app.
custom_bp should not be imported here nor used as a blueprint. It's more like a template for other routes (abstract class).
"""
