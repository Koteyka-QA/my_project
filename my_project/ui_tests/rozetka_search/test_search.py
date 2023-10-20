import pytest
from page_search import RozetkaPage
from conftest import browser
import time



@pytest.mark.test_search_on_rozetka
def test_search_on_rozetka(browser):
    rozetka = RozetkaPage(browser)
    rozetka.open()
    time.sleep(5)

    search_query = ""
    rozetka.enter_search_query(search_query)
    rozetka.click_search_button()

    assert "excepted result" in browser.page_source