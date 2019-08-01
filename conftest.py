import pytest
import random
import string


@pytest.fixture(scope='session')
def strings():
    test_string = "".join(random.choice(string.ascii_letters) for i in range(5))
    yield test_string
    print(f'String = {test_string}')


@pytest.fixture(scope='module')
def lists():
    test_range = 10
    test_list = [int(random.choice(string.digits)) for i in range(test_range)]
    yield test_list, test_range
    print(f'List = {test_list}')


@pytest.fixture
def ints():
    start = 0
    stop = 10
    test_int = random.randint(start, stop)
    yield start, stop, test_int
    print(f'Int = {test_int}')


@pytest.fixture
def dicts():
    dict_length = 5
    test_dict = {random.choice(string.digits): random.choice(string.ascii_letters) for i in range(dict_length)}
    yield test_dict, dict_length
    print(f'Dict = {test_dict}')


@pytest.fixture
def tuples():
    test_range = 10
    test_tuple = [int(random.choice(string.digits)) for i in range(test_range)]
    yield test_tuple, test_range
    print(f'List = {test_tuple}')