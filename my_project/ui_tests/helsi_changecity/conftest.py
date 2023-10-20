import pytest
from selenium import webdriver
from page_changecity import PageChangeCity

@pytest.fixture(scope="function")
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def page_changecity(chrome_browser):
    page = PageChangeCity(chrome_browser)
    page.open("https://helsi.me/clinics/kyiv")
    yield page
