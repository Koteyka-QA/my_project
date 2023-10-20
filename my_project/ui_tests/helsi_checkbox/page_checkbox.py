
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PageHelsiClinics:
    __URL = 'https://helsi.me/clinics/kyiv'
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__checkbox_label_text = "Державні"

    def open(self):
        self.__driver.get(self.__URL)

    def is_checkbox_selected(self, label_text):
        checkbox_xpath = f'//span[contains(@class, "InputCheckBox_label-text__yFbJp") and text()="{label_text}"]/preceding-sibling::input'
        checkbox = self.__driver.find_element(By.XPATH, checkbox_xpath)
        return checkbox.is_selected()

    def select_checkbox_by_label_text(self, label_text):
        checkbox_xpath = f'//span[contains(@class, "InputCheckBox_label-text__yFbJp") and text()="{label_text}"]/preceding-sibling::input'
        checkbox = self.__driver.find_element(By.XPATH, checkbox_xpath)
        if not checkbox.is_selected():
            checkbox.click()

    def select_checkbox(self):
        pass
