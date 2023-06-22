import requests
import pytest
from backend.settings import PYTEST_BASE_URL

access_token = ""
cookies = {}


def test_register():
    global id
    url = PYTEST_BASE_URL + "/user/register/"
    data = {
        "name": "abc",
        "email": "abc@abc.abc",
        "password": "abc",
        "username": "abc123",
    }
    response = requests.post(url=url, data=data)
    id = response.json()["id"]
    assert response.status_code == 200
    response = requests.post(url=url, data=data)
    assert response.status_code == 400


@pytest.fixture
def test_login():
    global access_token
    global cookies
    url = PYTEST_BASE_URL + "/user/login/"
    data = {
        "email": "abc@abc.abc",
        "password": "abcd",
    }
    response = requests.post(url=url, data=data)
    assert response.status_code == 403
    data = {
        "email": "abc@abc.abc",
        "password": "abc",
    }
    response = requests.post(url=url, data=data)
    for c in response.cookies:
        cookies[c.name] = c.value
    access_token = "Bearer " + response.json()["token"]
    assert response.status_code == 200
    return access_token


def test_get_user(test_login):
    global access_token
    global id
    _ = test_login
    url = PYTEST_BASE_URL + "/user"
    response = requests.get(url, headers={"Authorization": access_token})
    id = response.json()["user"]["id"]
    assert response.status_code == 200
    assert response.json()["user"]["email"] == "abc@abc.abc"
