"""
Tests for https://jsonplaceholder.typicode.com/ API
"""

import requests
import pytest
import re

BASE_URL = 'https://jsonplaceholder.typicode.com'


@pytest.mark.parametrize('resource, count',
                         [('posts', 100), ('comments', 500), ('albums', 100),
                          ('photos', 5000), ('todos', 200), ('users', 10)])
def test_json_1(resource, count):
    result = requests.get(BASE_URL+'/'+resource).json()
    assert len(result) == count


@pytest.mark.parametrize('id', [1, 10, 100])
def test_json_2(id):
    result = requests.get(BASE_URL+'/posts'+f'/{id}').json()
    assert result['id'] == id


@pytest.mark.parametrize('postId', [2, 5, 100])
def test_json_3(postId):
    params = {'postId': f'{postId}'}
    results = requests.get(url=BASE_URL+'/comments', params=params).json()
    for result in results:
        assert int(result['postId']) == postId


@pytest.mark.parametrize('user_id, name', [(1, 'Leanne Graham'), (2, 'Ervin Howell')])
def test_json_4(user_id, name):
    result = requests.get(BASE_URL+'/users'+f'/{user_id}').json()
    assert result['name'] == name


@pytest.mark.parametrize('postId', [-1, 0, 101])
def test_json_5(postId):
    params = {'postId': f'{postId}'}
    results = requests.get(url=BASE_URL+'/comments', params=params).json()
    assert results == []