class General:
    __abstract__ = True
    """
    ################################################################
    FLASK CONFIGURATION
    ################################################################
    """

    TESTING = False
    DEBUG = False
    SECRET = "This is a secret key and should be changed"

    """
    ################################################################
    LOGGING CONFIGURATION
    ################################################################
    """

    LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    LOG_DIR = "logs"  # Directory where logs are saved
    LOG_WHEN = "midnight"  # Moment where to log are cleared. Check logging.handlers.TimedRotatingFileHandler for more details
    LOG_BACKUP_COUNT = 3  # Number of backups
    LOG_INTERVAL = 1  # Interval

    """
    ################################################################
    DATA CONSTANTS CONFIGURATION
    ################################################################
    """
    NAME_LENGTH = 10
    DESCRIPTION_LENGTH = 50
