import pytest

import requests

from config import BASE_URL

@pytest.fixture
def user_response():
    response = requests.get(f'{BASE_URL}/users/1')
    return response


@pytest.fixture()
def delete_user():
    response = requests.delete(f'{BASE_URL}/users/1')
    return response

