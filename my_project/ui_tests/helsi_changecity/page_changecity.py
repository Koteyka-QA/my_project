import self
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PageChangeCity:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def change_city(self, new_city):
        city_select_xpath = '//div[@class="city-select-container CitySelect_container__5iglF"]'
        self.driver.find_element(By.XPATH, city_select_xpath).click()

        city_option_xpath = f'//div[@class="CitySelect_display-container__4tkW0"]' \
                            f'/div[@class="CitySelect_display-name__mtdG8" and text()="{new_city}"]'
        assert isinstance(self.driver.find_element(By.XPATH, city_option_xpath).click, object)
        self.driver.find_element(By.XPATH, city_option_xpath).click()