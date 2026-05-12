import requests

from config import BASE_URL


def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    return response


def update_user(user_id, body):
    response = requests.put(f'{BASE_URL}/users/{user_id}',json=body)

    return response


def patch_user(user_id, body):
    response = requests.patch(f'{BASE_URL}/users/{user_id}',
                              json = body)

    return response
