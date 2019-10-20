"""
Settings for fixtures managing, adding options to tests
"""
import os

import pytest
from fixtures.browser import Browser
from fixtures.db import DataBase


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="http://127.0.0.1",
        action="store",
        help="This is application base url")
    parser.addoption(
        "--browser",
        default='chrome',
        action='store',
        help='Browser to run tests')
    parser.addoption(
        "--imp_wait",
        default='60',
        action='store',
        help='Implicit wait time for browser, seconds'
    )
    

@pytest.fixture(scope="session")
def browser(request):
    base_url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    imp_wait = request.config.getoption("--imp_wait")
    fixture = Browser(base_url=base_url, browser=browser, imp_wait=imp_wait)
    yield fixture
    fixture.quit()


@pytest.fixture(scope="session")
def db():
    db_config = {
        'host': 'localhost',
        'name': 'bitnami_opencart',
        'user': 'bn_opencart',
        'password': '',
        'port': 8083
    }
    dbfixture = DataBase(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                         password=db_config['password'], port=int(db_config['port']))
    yield dbfixture
    dbfixture.destroy()


def pytest_configure(config):
    config._metadata['os'] = os.name
    config._metadata['PATH'] = os.environ['PATH']
    config._metadata['pwd'] = os.getcwd()

