"""
Module for tests with lists objects
"""


def test_lists(lists):
    """
    Test checks length of generated list and length parameter for list generation
    """
    assert lists[1] == len(lists[0])


def test_lists_2(strings, lists):
    """
    Test checks strings fixture type and lists type are not equal
    """
    assert not isinstance(strings, type(lists))
