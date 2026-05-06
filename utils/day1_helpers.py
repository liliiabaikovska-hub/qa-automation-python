def check_age(age):
    if age < 18:
        return "Access denied"
    return "Access granted"


def check_status(status_code):
    if status_code == 200:
        return "OK"
    elif status_code == 404:
        return "Not Found"
    else:
        return "Unknown status"


def get_user_name(user):
    return user['name']


def get_user_name_safe(user):
    if 'name' in user:
        return user['name']
    return 'Unknown'
