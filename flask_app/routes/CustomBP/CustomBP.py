from flask import Blueprint, current_app


class CustomBP(Blueprint):
    """
    CustomBP: A base class for specialized Blueprint management in Flask.

    This class extends Flask's Blueprint to provide additional features tailored
    for modular Flask applications. It serves as a foundation for creating
    specialized Blueprints with added functionality, such as managing test-specific
    or feature-specific routes.

    Key Features:
    --------------
    1. **Instance Management:**
       - Ensures that only one instance of a Blueprint with the same name exists
         per subclass (Singleton pattern by name).
       - Keeps track of all instances created for a subclass, enabling easy access.

    2. **Centralized Loading:**
       - Provides methods to register all instances of a subclass (`load_all`) or
         an individual instance (`load`) into a Flask application.
       - Simplifies the process of managing and registering multiple Blueprints.

    Intended Usage:
    ---------------
    - This class is designed to be extended by specialized Blueprint subclasses
      (e.g., for handling test-related routes or feature-specific modules).
    - Developers can define their own behavior by inheriting from `CustomBP` and
      adding their specific logic or configurations.

    Example:
    --------
    ```python
    from flask import Flask
    from custom_bp import CustomBP

    # Create a specialized Blueprint subclass
    class TestBP(CustomBP):
        pass

    # Define Blueprints using the specialized class
    test_bp1 = TestBP(name="test_bp1", import_name=__name__)
    test_bp2 = TestBP(name="test_bp2", import_name=__name__)

    # Add routes (example)
    @test_bp1.route("/test1")
    def test1():
        return "This is test1"

    # Register all TestBP instances into the Flask app
    app = Flask(__name__)
    TestBP.load_all(app)

    if __name__ == '__main__':
        app.run(debug=True)
    """

    _instances = {}

    # __abstract__ = True

    def __new__(cls, *args, **kwargs):
        # Initialiser la liste des instances pour cette sous-classe, si ce n'est pas déjà fait
        if cls not in cls._instances:
            cls._instances[cls] = []

        # check if an instance with the same name already exists
        for instance in cls._instances[cls]:
            if instance.name == kwargs.get('name'):
                return instance

        # Create a new instance and add it to the list
        instance = Blueprint(*args, **kwargs)
        cls._instances[cls].append(instance)
        # Log the creation of the Blueprint instance
        current_app.logger.info(f'Blueprint {instance.name} created')

        return instance

    def load(self, app):
        """Register this instance into the Flask app."""
        app.register_blueprint(self)
        app.logger.info(f'Blueprint {self.name} loaded')

    @classmethod
    def get_instances(cls):
        """Get all instances specific to this subclass."""
        return cls._instances.get(cls, [])

    @classmethod
    def load_all(cls, app):
        """Register all instances of this subclass into the Flask app."""
        for instance in cls.get_instances():
            app.register_blueprint(instance)
            app.logger.info(f'Blueprint {instance.name} loaded')
        return cls.get_instances()
