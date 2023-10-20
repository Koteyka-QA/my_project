import pytest
from api_reqres import APIClient


@pytest.fixture(scope="module")
def api_client():
    base_url = "https://reqres.in"
    path = "/api/users/2"
    headers = {
        "Content-Type": "application/json",
    }
    json_data = {
        "name": "morpheus",
        "job": "zion resident",
    }
    return APIClient(base_url, path, headers, json_data)