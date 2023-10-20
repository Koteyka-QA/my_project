import pytest
from page_checkbox import PageHelsiClinics

class TestCheckbox:

    def test_select_checkbox(self, browser):
        page = PageHelsiClinics(browser)
        page.open()
        page.select_checkbox()
        assert page.is_checkbox_selected()