"""
Module for tests with dictionary objects
"""


def test_dict(dicts):
    """
    Test checks length og generated dict equal generator range
    """
    assert len(dicts[0]) == dicts[1]


def test_dict_2(dicts):
    """
    Test checks list function extract dict keys
    """
    test_dict_keys = list(dicts[0])
    assert test_dict_keys == list(dicts[0].keys())
