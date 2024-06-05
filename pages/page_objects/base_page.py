"""Модуль содержит PageObject BasePage"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_elements.elements import Button, Input
from pages.page_components.catalog_menu import CatalogMenuComponent
from pages.page_components.search_bar import SearchBarComponent


class BasePage:
    """PageObject BasePage"""

    def __init__(self, browser: webdriver, url: str, timeout: float = 10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

        self.__catalog_menu = CatalogMenuComponent(browser)
        self.__catalog_menu_button = Button(
            browser,
            name="button_calls_catalog_menu",
            locator=(By.CSS_SELECTOR, ".dropdown-catalog-btn"),
        )
        self.__search_bar = SearchBarComponent(browser)

    @property
    def current_url(self) -> str:
        """Получить URL страницы"""
        return self.browser.current_url

    def open(self):
        """Открыть станицу."""
        self.browser.get(self.url)
        return self

    def open_catalog_menu(self):
        self.__catalog_menu_button.click_to_button()
        return self.__catalog_menu

    def perform_search_query(self, search_query: str):
        self.__search_bar.input_text(search_query)
        self.__search_bar.submit_button_click()

    def select_by_search_query(self, search_query: str, list_index: str, item_index: str):
        self.__search_bar.input_text(search_query)
        self.__search_bar.select_dropdown_item_by_index(list_index, item_index)
