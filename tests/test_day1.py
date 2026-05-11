import pytest
from utils.day1_helpers import (
    check_age,
    check_status,
    get_user_name,
    get_user_name_safe
)


def test_age_allowed():
    assert check_age(20) == "Access granted"


def test_age_denied():
    assert check_age(15) == "Access denied"


def test_age_boundary():
    assert check_age(18) == "Access granted"



def test_status_200():
    assert check_status(200) == 'OK'


def test_status_404():
    assert check_status(404) == 'Not Found'


def test_status_unknown():
    assert check_status(405) == 'Unknown status'


def test_get_user_name():
    user = {
        'name': 'Liliya',
        'age': 25
    }
    assert get_user_name(user) == 'Liliya'


def test_get_user_name_other():
    user = {
        'name': 'Ivan',
        'age': 20
    }
    assert get_user_name(user) == 'Ivan'


def test_get_user_name_no_name():
    user = {
        'age': 20
    }
    with pytest.raises(KeyError):
        get_user_name(user)


def test_get_user_name_safe_ok():
    user = {'name': 'Liliya'}
    assert get_user_name_safe(user) == 'Liliya'


def test_get_user_name_safe_no_name():
    user = {}
    assert get_user_name_safe(user) == 'Unknown'
