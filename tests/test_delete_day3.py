import requests

from config import BASE_URL

def test_delete_user(delete_user):

    assert delete_user.status_code==200


def test_delete_user_empty_response(delete_user):


    data = delete_user.json()
    assert data == {}


def test_delete_non_existing_user():
    response = requests.delete(f'{BASE_URL}/users/9999')
    assert response.status_code == 200

def test_delete_user_content_type(delete_user):

    assert delete_user.headers['Content-Type'] == "application/json; charset=utf-8"


def test_delete_user_response_time(delete_user):
    assert delete_user.elapsed.total_seconds()<1
