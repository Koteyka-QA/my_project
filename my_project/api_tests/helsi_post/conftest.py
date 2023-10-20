import pytest
from api_helsi import APIClient


@pytest.fixture(scope="module")
def api_client():
    base_url = "https://api.segment.io"
    path = "/v1/p"
    headers = {
        "authority": "api.segment.io",
    }
    json_data = {"success": True}
    return APIClient(base_url, path, headers, json_data)
