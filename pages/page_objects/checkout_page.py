"""Модуль содержит PageObject MainPage"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page_objects.base_page import BasePage
from pages.page_components.cart import Cart
from pages.page_elements.elements import BaseElement
from data.pages_links import BASKET_PAGE_LINK


class CheckoutPage(BasePage):
    """Класс PageObject CatalogPage"""

    url = BASKET_PAGE_LINK

    def __init__(self, browser: webdriver, url: str = url, timeout: float = 10):
        super().__init__(browser, url, timeout)

        self._empty_cart_img = BaseElement(
            self.browser, name="empty cart img", locator=(By.CSS_SELECTOR, ".container img.empty-page-img")
        )

        self.__cart = Cart(self.browser)

    @property
    def cart(self):
        """Returns: Card with products on the CheckoutPage"""
        return self.__cart

    def is_cart_empty(self):
        """"
        Returns:
            True - if is cart empty
            False - if is cart not empty
        """
        return self._empty_cart_img.is_element_present()
