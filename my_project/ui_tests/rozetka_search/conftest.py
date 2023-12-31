import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver



@pytest.fixture
def browser():
    driver: WebDriver = webdriver.Chrome()
    yield driver
    driver.quit()