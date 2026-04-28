import requests 

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user():
    return requests.get(f"{BASE_URL}/users")
