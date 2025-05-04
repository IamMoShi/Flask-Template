from app.routes.user_routes import user_bp


def register_blueprint(app, blueprint):
    """Register a blueprint."""
    app.register_blueprint(blueprint)
    app.logger.info(f"{blueprint.name} registered")


def register_routes(app):
    """Register all blueprints."""
    app.logger.info("Registering routes")
    register_blueprint(app, user_bp)
