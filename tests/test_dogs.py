"""
Tests for https://dog.ceo/dog-api/ API
"""

import re
import requests
import pytest


def test_dog_1():
    result = requests.get('https://dog.ceo/api/breeds/list/all').json()
    assert result['status'] == 'success'


def test_dog_2():
    result = requests.get('https://dog.ceo/api/breeds/list/all').json()
    assert 'akita' in result['message']


@pytest.mark.parametrize('count', [1, 2, 3, 4])
def test_dog_3(count):
    result = requests.get(f'https://dog.ceo/api/breeds/image/random/{count}').json()
    assert len(result['message']) == count


def test_dog_4():
    result = requests.get('https://dog.ceo/api/breed/akita/images/random')
    assert result.headers['Content-Type'] == 'application/json'


@pytest.mark.parametrize('dogs', ["affenpinscher", "african", "airedale", "akita", "borzoi"])
def test_dog_5(dogs):
    result = requests.get(f'https://dog.ceo/api/breed/{dogs}/images/random').json()
    assert re.search('\.(jpg)$', result['message'])
