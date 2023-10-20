import pytest
from login_page import LoginPage

# post.login
@pytest.fixture(scope='session')
def login_page():
    login = LoginPage()
    yield login
    login.cleanup()

