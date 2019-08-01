"""
Module for tests with integer objects
"""


def test_int(ints):
    """
    Test checks ints is lte end of range and gte start of range
    """
    assert ints[2] <= ints[1]
    assert ints[2] >= ints[0]


def tes_int_2(ints):
    """
    Test checks ints generated in range between start and stop
    """
    assert ints[2] in range(ints[0], ints[1])
