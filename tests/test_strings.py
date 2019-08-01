"""
Module for tests with string objects
"""


def test_strings(strings):
    """
    Test checks length of string
    """
    test_string = strings * 2
    assert len(test_string) == 10


def test_strings_2(strings):
    """
    Test checks string has type str
    """
    assert isinstance(strings, str)
