import time
import pytest
from selenium.webdriver.common.by import By
from page_dropdown import PageTabletki

@pytest.mark.parametrize("browser", ["chrome", "firefox"], indirect=True)
def test_open_pharmacy_nearby(browser):
    page = PageTabletki(browser)
    browser.get("https://tabletki.ua/")

    page.open_services_menu()
    services_menu = page.driver.find_element(By.XPATH, '//div[@id="menuServicesModal"]')
    time.sleep(5)
    page.open_pharmacy_nearby()
    assert page.driver.current_url == "https://tabletki.ua/uk/pharmacy/kiev/"