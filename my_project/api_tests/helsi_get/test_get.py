import pytest

@pytest.mark.test_get_api_data
def test_get_api_data(api_client):
    response = api_client.get_data()
    assert response.status_code == 200
    data = response.json()
    assert "telemedicine_requests" in data["data"]