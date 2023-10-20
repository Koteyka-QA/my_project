def test_put_api_data(api_client):
    response = api_client.put_data()
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "zion resident"