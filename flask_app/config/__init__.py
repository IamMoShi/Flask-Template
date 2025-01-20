from flask_app.config.development_configs import DevelopmentConfigSQLite
from flask_app.config.production_configs import ProductionConfig
from flask_app.config.test_configs import UnitTestConfig, IntegrationTestConfig

"""
Add other configuration class to be used in the dedicated file and import them here
Only import fully qualified configuration
Example: 
    General config is not a fully qualified configuration, 
    it should not be used directly in the application,
    that's why it is not imported here 
"""
