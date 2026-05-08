import requests
from config import BASE_URL

TEST_USER = {
    "name": "Irina",
    "job": "QA"
}
UPDATED_USER = {
    "name": "Irina",
    "job": "Senior QA"
}


def test_get_user_status_code(user_response):
    assert user_response.status_code == 200


def test_get_user_id(user_response):
    data = user_response.json()

    assert data['id'] == 1


def test_get_user_has_name(user_response):
    data = user_response.json()

    assert 'name' in data


def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404


def test_create_user_status_code():
    response = requests.post(f'{BASE_URL}/users', json=TEST_USER)

    assert response.status_code == 201


def test_create_user_check_name():
    response = requests.post(f'{BASE_URL}/users', json=TEST_USER)
    data = response.json()

    assert data['name'] == TEST_USER['name']


def test_create_user_check_job():
    response = requests.post(f'{BASE_URL}/users', json=TEST_USER)
    data = response.json()

    assert data['job'] == TEST_USER['job']


def test_update_user_job():
    response = requests.put(f"{BASE_URL}/users/1", json=UPDATED_USER)
    data = response.json()
    assert response.status_code == 200
    assert data['job'] == UPDATED_USER['job']
