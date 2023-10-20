import pytest
from api_delete import APIClient


@pytest.fixture(scope="module")
def api_client():
    base_url = "https://reqres.in"
    path = "/api/users/100"
    headers = {
        "Content-Type": "application/json",
    }
    return APIClient(base_url, path, headers)