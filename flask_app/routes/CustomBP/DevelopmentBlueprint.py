from flask_app.routes.CustomBP.CustomBP import CustomBP


class DevelopmentBlueprint(CustomBP):
    """
    Blueprint for development environment.
    """
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
