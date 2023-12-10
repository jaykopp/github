import requests

def profile():
    requests.get('https://api.github.com/user', auth=('user', 'pass'))

def my_profile():
    requests.get('https://api.github.com/user', auth=('user', 'pass'))