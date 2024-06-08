"""The module contains PageComponent SearchBar"""

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_elements.elements import InputField, Button


class SearchBar:
    """
    PageComponent SearchBar
    Search bar on Main, Catalog, Product pages
    """
    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "Dropdown catalog menu"
        self.__input_form = InputField(
            browser,
            name="search_bar",
            locator=(By.CSS_SELECTOR, "form.head-search > input"),
        )
        self.__submit_button = Button(
            browser,
            name="search_bar",
            locator=(By.CSS_SELECTOR, "button.head-search__btn"),
        )

    def input_text(self, text: str):
        """
        Input text in search bar
        Parameters: text
        Returns: self
        """
        logger.info(f"Input text to search bar {text}")
        self.__input_form.input_text(text)
        return self

    def click_submit_button(self):
        """
        Click on submit button in search bar
        Returns: self
        """
        logger.info(f"Click on submit button in search bar")
        self.__submit_button.click_to_button()
        return self
