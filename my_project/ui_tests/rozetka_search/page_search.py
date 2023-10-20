from selenium.webdriver.common.by import By



class RozetkaPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://rozetka.com.ua/ua/dacha-sad-ogorod/c2394297/"
        self.search_input = (By.NAME, "search")
        self.search_button = (By.CLASS_NAME, "search-form__submit")

    def open(self):
        self.driver.get(self.url)
    def enter_search_query(self, query):
        search_box = self.driver.find_element(*self.search_input)
        search_box.send_keys(query)

    def click_search_button(self):
        search_button = self.driver.find_element(*self.search_button)
        search_button.click()



