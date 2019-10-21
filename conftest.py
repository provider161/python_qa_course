"""
Settings for fixtures managing, adding options to tests
"""
import os

import pytest
import paramiko
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


@pytest.fixture(scope="session")
def ssh_client():
    ssh_conf = {
        'host': '0.0.0.0',
        'user': 'user',
        'pass': 'user',
        'port': 8082
    }
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ssh_conf['host'], username=ssh_conf['user'],
                   password=ssh_conf['pass'], port=ssh_conf['port'])
    yield client
    client.close()


def pytest_configure(config):
    config._metadata['os'] = os.name
    config._metadata['PATH'] = os.environ['PATH']
    config._metadata['pwd'] = os.getcwd()

