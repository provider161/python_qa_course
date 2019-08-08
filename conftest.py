import pytest
from fixtures.api import APIClient


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        action="store",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_url=base_url)