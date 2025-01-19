import os

import pytest


def integration_test():
    # Set the FLASK_ENV environment variable to testing
    os.environ['FLASK_ENV'] = 'testing'

    # Set the TEST_TYPE environment variable to unit
    # Check else if in conftest.py
    os.environ['TEST_TYPE'] = 'integration'

    # Define the path to the unit tests
    pytest_args = ["Tests/tests_flask_app/integration"]
    pytest.main(pytest_args)


if __name__ == '__main__':
    integration_test()
