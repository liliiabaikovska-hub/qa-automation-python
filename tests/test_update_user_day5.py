import requests

from utils.api_helpers import update_user
from utils.api_helpers import patch_user

UPDATED_USER = {
    "name": "Irina",
    "job": "Senior QA"
}

PATCH_USER = {
    "job": "Lead QA"
}
PATCH_NO_USER = {}


def test_update_user_status_code():
    response = update_user(1,UPDATED_USER)

    assert response.status_code == 200


def test_update_user_check_job():
    response = update_user(1,UPDATED_USER)
    data = response.json()
    assert data['job'] == "Senior QA"




def test_patch_user_status_code():
    response = patch_user(1, PATCH_USER)

    assert response.status_code == 200
def test_patch_user_job():
    response = patch_user(1,PATCH_USER)

    data = response.json()

    assert data['job'] == 'Lead QA'












