import logging
import os
from logging.handlers import TimedRotatingFileHandler

from flask import Flask


def setup_logging(app: Flask) -> None:
    """
    Configure the logger of the flask app
    :param app: Flask application
    :return: None
    """

    """
    ################################################################
    Load info from app configuration
    Check for field starting by "LOG_" in configuration
    ################################################################
    """
    missing_fields: [str] = []

    def get_config_info(key, default):
        """
        Get configuration information
        And save missing fields for logging
        Can log right away because logger is not setup yet
        :param key: The key to get from configuration
        :param default: Default value if key is not found
        :return: Value of the key (equivalent to app.config.get(key, default) but with logging)
        """
        if key not in app.config:
            try:
                missing_fields.append(str(key))
            except TypeError as e:
                missing_fields.append(f"Incompatible key : {e}")
        return app.config.get(key, default)

    # Format used to save logs
    log_format: str = get_config_info("LOG_FORMAT", "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s")
    # Directory where logs are saved
    log_dir: str = get_config_info("LOG_DIR", "logs")
    # Moment where to log are cleared. Check logging.handlers.TimedRotatingFileHandler for more details
    log_when: str = get_config_info("LOG_WHEN", "midnight")
    # Number of backups
    log_backup_count: int = get_config_info("LOG_BACKUP_COUNT", 3)
    # Interval
    log_interval: int = get_config_info("LOG_INTERVAL", 1)

    """
    ################################################################
    Configure logger
    ################################################################
    """

    # Create
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # --------------------------------------------------------------
    # Handler for DEBUG and INFO

    info_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "info.log"),
        when=log_when,
        interval=log_interval,
        backupCount=log_backup_count
    )

    info_handler.setLevel(logging.INFO)  # Save only INFO and above
    info_handler.setFormatter(logging.Formatter(log_format))

    # --------------------------------------------------------------
    # Handler for WARNING

    warning_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "warning.log")
    )

    warning_handler.setLevel(logging.WARNING)  # Save only WARNING and above
    warning_handler.setFormatter(logging.Formatter(log_format))

    # --------------------------------------------------------------
    # Handler for ERROR

    error_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "error.log")
    )

    error_handler.setLevel(logging.ERROR)  # Save only ERROR and above
    error_handler.setFormatter(logging.Formatter(log_format))

    # --------------------------------------------------------------
    # Handler for CRITICAL

    critical_handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "critical.log")
    )

    critical_handler.setLevel(logging.CRITICAL)  # Save only CRITICAL and above
    critical_handler.setFormatter(logging.Formatter(log_format))

    # --------------------------------------------------------------
    # Adding handlers to logger root
    # --------------------------------------------------------------
    root_logger: logging.Logger = logging.getLogger()

    root_logger.setLevel(logging.DEBUG)  # Minimal level
    root_logger.addHandler(info_handler)
    root_logger.addHandler(warning_handler)
    root_logger.addHandler(error_handler)
    root_logger.addHandler(critical_handler)

    # --------------------------------------------------------------
    # Logging to console (development mode only)
    # --------------------------------------------------------------

    if app.debug:
        console_handler: logging.StreamHandler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(logging.Formatter(log_format))
        root_logger.addHandler(console_handler)

    # --------------------------------------------------------------
    # Log missing fields and end of setup
    # --------------------------------------------------------------

    for field in missing_fields:
        app.logger.warning(f"Missing field in configuration: {field}")

    app.logger.info("Logging setup complete")
