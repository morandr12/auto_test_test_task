"""The module contains PageObject MainPage"""

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_objects.base_page import BasePage
from pages.page_elements.elements import Button
from pages.page_components.catalog_menu import CatalogMenu
from pages.page_components.search_bar import SearchBar
from data.pages_links import MAIN_PAGE_LINK


class MainPage(BasePage):
    """PageObject MainPage"""

    url = MAIN_PAGE_LINK

    def __init__(self, browser: webdriver, url: str = url, timeout: float = 10):
        super().__init__(browser, url, timeout)
        self.__catalog_menu = CatalogMenu(browser)
        self.__catalog_menu_button = Button(
            browser,
            name="button_calls_catalog_menu",
            locator=(By.CSS_SELECTOR, ".dropdown-catalog-btn"),
        )
        self.__search_bar = SearchBar(browser)

    @property
    def search_bar(self) -> SearchBar:
        """ Return: Search bar on Main, Catalog, Product pages """
        return self.__search_bar

    def open_catalog_menu(self) -> CatalogMenu:
        """
        Open CatalogMenu
        Return: CatalogMenu - Dropdown menu with catalogs
        """
        logger.info("Open catalog menu")
        self.__catalog_menu_button.click_to_button()
        return self.__catalog_menu
