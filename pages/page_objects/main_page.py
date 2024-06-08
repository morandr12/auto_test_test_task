"""The module contains PageObject MainPage"""

from selenium import webdriver
from pages.page_objects.base_page import BasePage
from pages.components.header import Header
from data.pages_links import MAIN_PAGE_LINK


class MainPage(BasePage):
    """PageObject MainPage"""

    url = MAIN_PAGE_LINK

    def __init__(self, browser: webdriver, url: str = url):
        super().__init__(browser, url)
        self.__header = Header(browser)

    @property
    def header(self) -> Header:
        """ Return: Header"""
        return self.__header
