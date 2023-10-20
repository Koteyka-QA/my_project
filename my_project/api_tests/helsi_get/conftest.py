import pytest
from api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    base_url = "https://helsi.me"
    path = "/api/healthy/applications/pisclient/features?sid=1"
    headers = {
        "authority": "helsi.me",
    }
    return APIClient(base_url, path, headers)

