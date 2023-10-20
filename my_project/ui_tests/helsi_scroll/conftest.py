import pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v116 import page

@pytest.fixture(scope="function")
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def helsi_page(chrome_browser):
    page.open("https://helsi.me/clinics/kyiv")
    yield page