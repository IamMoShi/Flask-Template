import time

from sqlalchemy.exc import OperationalError

from app import db


def wait_for_db(app, max_retries=10, delay=2):
    """This function will wait until the database is available or if it reached
    max retries."""
    for i in range(max_retries):
        try:
            with app.app_context():
                db.create_all()
            return
        except OperationalError:
            app.logger.warning(
                f"Database not ready. Retry {i + 1}/{max_retries}..."
            )
            time.sleep(delay)
    raise RuntimeError("Database not available after retries")
