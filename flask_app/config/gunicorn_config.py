import os

from flask_app.config.production_configs import ProductionConfig as ProdConfig

log_dir: str = ProdConfig.LOGGING_DIRECTORY
os.makedirs(log_dir, exist_ok=True)

bind = "0.0.0.0:8000"
workers = 1
loglevel = ProdConfig.LOGGING_LEVEL
logconfig = ProdConfig.LOGGING_CONFIGURATION_FILE
