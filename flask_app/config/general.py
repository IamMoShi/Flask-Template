class General:
    __abstract__ = True

    """
    ################################################################
    FLASK CONFIGURATION
    ################################################################
    """

    TESTING: bool = False
    DEBUG: bool = False
    SECRET: str = "This is a secret key and should be changed"

    """
    ################################################################
    LOGGING CONFIGURATION
    ################################################################
    """

    # Check the dedicated logging configuration file
    LOGGING_CONFIGURATION_FILE: str = "flask_app/config/logging.conf"
    LOGGING_DIRECTORY: str = "logs"
    LOGGING_LEVEL: str = "info"
