import requests
from backend.settings import PYTEST_BASE_URL
from Users.test_users import test_login


def test_post_job_application(test_login):
    url = PYTEST_BASE_URL + "/job-application/"
    access_token = test_login
    data = {
        "company_name": "Google",
        "job_url": "a@a.com",
        "status": "Interview",
    }
    response = requests.post(
        url=url,
        data=data,
        headers={"Authorization": access_token},
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json()["status"] == "Interview"


def test_get_job_application(test_login):
    url = PYTEST_BASE_URL + "/job-application"
    access_token = test_login
    response = requests.get(
        url=url,
        headers={"Authorization": access_token},
    )
    assert response.status_code == 200
    response = requests.get(
        url=url,
    )
    assert response.status_code == 403
