
def test_post_api_data(api_client):
    response = api_client.post_data()
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True