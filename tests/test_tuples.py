"""
Module for tests with tuples objects
"""


def test_tuple(tuples):
    """
    Test checks range of generated tuple
    """
    count = 0
    for _ in tuples[0]:
        count += 1
    assert count == tuples[1]


def test_tuple_2(tuples):
    """
    Test checks length of doubled tuple equal length doubled generation range
    """
    assert len(tuples[0]) * 2 == tuples[1] * 2
