import pytest

# post.login
@pytest.mark.test_login_successful
def test_login_successful(login_page):
    email = "eve.holt@reqres.in"
    password = "cityslicka"

    response = login_page.login(email, password)

    assert response.status_code == 200
    assert "token" in response.json()
    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"

@pytest.mark.test_login_unsuccessful
def test_login_unsuccessful(login_page):
    email = "eve.holt@reqres.in"
    password = "wrong_password"
    response = login_page.login(email, password)

    assert response.status_code !=200








