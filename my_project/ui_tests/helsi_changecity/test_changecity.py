from selenium.webdriver.common.by import By


def test_change_city(page_changecity):
    new_city = "Житомир"
    page_changecity.change_city(new_city)

    city_select_xpath = '//div[@class="city-select-container CitySelect_container__5iglF"]'
    selected_city_xpath = f'{city_select_xpath}//div[@class="CitySelect_display-name__mtdG8"]'
    selected_city = page_changecity.driver.find_element(By.XPATH, selected_city_xpath).text
    assert selected_city == new_city