def test_delete_api_data(api_client):
    response = api_client.delete_data()
    assert response.status_code == 204