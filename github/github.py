import requests

def get_profile(user):
    r = requests.get(f'https://api.github.com/users/{user}')
    return r

def profile(user):
    profile_content = get_profile(user).json()


def my_profile():
    requests.get('https://api.github.com/user', auth=('user', 'pass'))