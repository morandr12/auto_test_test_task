"""Модуль содержит PageObject MainPage"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_objects.base_page import BasePage
from data.pages_links import MAIN_PAGE_LINK


class MainPage(BasePage):
    """Класс PageObject MainPage"""

    url = MAIN_PAGE_LINK

    def __init__(self, browser: webdriver, url: str = url, timeout: float = 10):
        super().__init__(browser, url, timeout)
