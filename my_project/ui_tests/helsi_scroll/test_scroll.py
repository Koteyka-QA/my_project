import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from page_scroll import PageHelsiClinics


def test_scroll_page(helsi_page):
    helsi_page.scroll_page(500)
    pass
