"""Модуль содержит PageObject MainPage"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_objects.base_page import BasePage
from pages.page_elements.elements import BaseElement
from pages.page_components.product_card import ProductCard


class CatalogPage(BasePage):
    """Класс PageObject CatalogPage"""

    def __init__(self, browser: webdriver, url: str, timeout: float = 10):
        super().__init__(browser, url, timeout)

        self.__header_with_catalog_name = BaseElement(
            self.browser,
            name="header_with_catalog_name",
            locator=(By.CSS_SELECTOR, "div.pt-0 h1"),
        )
        self.__breadcrumb_item = BaseElement(
            self.browser,
            name="breadcrumb_item_in_category_link_path",
            locator=(By.CSS_SELECTOR, "ul.breadcrumb__list > li.breadcrumb__item > a"),
        )

    @property
    def catalog_name(self) -> str:
        return self.__header_with_catalog_name.get_element().text

    @property
    def category_names_path(self):
        return [item.text for item in self.__breadcrumb_item.get_all_elements()]

    def get_product_card_by_id(self, product_id: str):
        return ProductCard(self.browser, product_id)

    def is_there_product_in_catalog(self, product_id: str):
        return self.get_product_card_by_id(product_id).find_product_card()
