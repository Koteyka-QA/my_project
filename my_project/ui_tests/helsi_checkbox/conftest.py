import pytest
from selenium import webdriver


@pytest.fixture(scope='browser')
def browser():
    driver = webdriver.Chrome()
    yield driver.quit()
