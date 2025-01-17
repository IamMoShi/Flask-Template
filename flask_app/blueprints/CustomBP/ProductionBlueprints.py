from flask_app.blueprints.CustomBP.CustomBP import CustomBP


class ProductionBlueprint(CustomBP):
    """
    ProductionBlueprint class.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
