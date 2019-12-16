"""
Tests for https://www.openbrewerydb.org API
"""

import requests
import pytest
import requests_mock

BASE_URL = 'https://api.openbrewerydb.org/breweries'


def response_get(params):
    return requests.get(BASE_URL, params=params)


@pytest.fixture
def mock():
    with requests_mock.Mocker() as mock_instance:
        yield mock_instance


def test_brewery_1(mock):
    params = {'by_city': 'Alameda'}
    mock.get(BASE_URL, json={'city': 'Alameda'})
    result = response_get(params=params).json()
    assert result['city'] == 'Alameda'


def test_brewery_2(mock):
    params = {'by_state': 'new_york'}
    mock.get(BASE_URL, json={'state': 'New York'})
    result = requests.get(BASE_URL, params=params).json()
    assert result['state'] == 'New York'


@pytest.mark.parametrize('breweries', [1, 2, 3, 10])
def test_brewery_3(breweries, mock):
    test_url = BASE_URL + f'/{breweries}'
    mock.get(test_url, json={'id': f'{breweries}'})
    result = requests.get(test_url).json()
    assert int(result['id']) == breweries
