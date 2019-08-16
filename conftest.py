"""
Settings for fixtures managing, adding options to tests
"""

import pytest
from fixtures.browser import Browser


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
        help='Browser to run tests'
    )
    

@pytest.fixture(scope="session")
def browser(request):
    base_url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    fixture = Browser(base_url=base_url, browser=browser)
    yield fixture
    fixture.quit()
