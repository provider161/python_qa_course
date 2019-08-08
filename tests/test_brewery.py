"""
Tests for https://www.openbrewerydb.org API
"""

import re
import requests
import pytest

BASE_URL = 'https://api.openbrewerydb.org/breweries'


def test_brewery_1():
    params = {'by_city': 'Alameda'}
    result = requests.get(BASE_URL, params=params).json()
    assert result[0]['city'] == 'Alameda'


def test_brewery_2():
    params = {'by_state': 'new_york'}
    result = requests.get(BASE_URL, params=params).json()
    assert result[0]['state'] == 'New York'


@pytest.mark.parametrize('breweries', [1, 2, 3, 10])
def test_brewery_3(breweries):
    result = requests.get(BASE_URL+f'/{breweries}').json()
    assert result['id'] == breweries


@pytest.mark.parametrize('search_names', ['dog', 'mad', 'beer'])
def test_brewery_4(search_names):
    params = {'query': f'{search_names}'}
    results = requests.get(BASE_URL+'/autocomplete', params=params).json()
    for result in results:
        assert re.search(f'(?i).*{search_names}.*', result['name'])


@pytest.mark.parametrize('search_cities', ['Oakland', 'New York', 'Chicago'])
def test_brewery_5(search_cities):
    params = {'search': f'{search_cities}'}
    results = requests.get(BASE_URL+'/autocomplete', params=params).json()
    for result in results:
        assert re.search(f'(?i).*{search_cities}.*', result['city'])
