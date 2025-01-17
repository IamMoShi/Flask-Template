class TestExemple:
    """
    ################################################################
    Test Class needs to start with Test.
    Test methods need to start with test.
    Those rules are naming conversions and are defined in pytest.ini

    It is possible to have multiple customisation check pytest
    documentation for more information.
    ################################################################
    """

    def test_example(self):
        assert 1 == 1
        assert "Test" == "Test"

    def test_example2(self):
        assert 2 == 2

    def test_example_fail(self):
        assert 1 == 2  # This test will fail
