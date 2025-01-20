from flask_app import dev, prod

# Import the config that you want to use in run.py file. Do not modify as RunConfig.
from flask_app.config import DevelopmentConfigSQLite as DevConfig
from flask_app.config import ProductionConfig as ProdConfig

if __name__ == "__main__":
    # Check in the environment variable to see if the app is running in production or development.
    # If the environment variable is not set, the app will run in development mode.
    import os

    if os.environ.get("FLASK_ENV") == "production":
        prod().run(host="0.0.0.0", port=ProdConfig.PORT)
    else:
        dev().run(host="0.0.0.0", port=DevConfig.PORT)
