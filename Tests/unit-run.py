import os

import pytest


def unit_test():
    # Set the FLASK_ENV environment variable to testing
    os.environ['FLASK_ENV'] = 'testing'

    # Set the TEST_TYPE environment variable to unit
    os.environ['TEST_TYPE'] = 'unit'

    # Define the path to the unit tests
    pytest_args = ["Tests/unit"]

    pytest.main(pytest_args)


if __name__ == '__main__':
    unit_test()
