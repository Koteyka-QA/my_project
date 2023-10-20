
from selenium.webdriver.remote.webdriver import WebDriver


class PageHelsiClinics:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def scroll_page(self, pixels):
        script = f"window.scrollBy(0, {pixels});"
        self.driver.execute_script(script)