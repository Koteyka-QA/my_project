
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageTabletki:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_services_menu(self):
        services_menu = self.driver.find_element(By.XPATH, '//div[@id="menuServicesModal"]')
        WebDriverWait(self.driver, 10).until(EC.visibility_of(services_menu))
    def is_services_menu_visible(self):
        services_menu = self.driver.find_element(By.XPATH, '//div[@id="menuServicesModal"]')
        return services_menu.is_displayed()

    def open_services_menu(self):
        services_button = self.driver.find_element(By.XPATH, '//button[text()="Сервіси"]')
        services_button.click()
