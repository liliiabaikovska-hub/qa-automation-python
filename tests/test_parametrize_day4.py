import pytest
from utils.day1_helpers import check_age, check_status


@pytest.mark.parametrize(
    'age, expected_result',
    [
        (15, "Access denied"),
        (18, "Access granted"),
        (25, "Access granted"),

    ]
)

def test_check_age(age,expected_result):
    result = check_age(age)
    assert result==expected_result




@pytest.mark.parametrize("status,expexted_result",
                         [
                             (200,'OK'),
                             (404,'Not Found'),
                             (405,'Unknown status'),
                             (-1,'Unknown status'),
                             (None,'Unknown status'),
                         ]
                         )
def test_status_code(status,expexted_result):
    result = check_status(status)
    assert result==expexted_result

