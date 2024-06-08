"""The module contains PageComponent ModalCart"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger
from pages.page_objects.checkout_page import CheckoutPage
from pages.page_elements.elements import BaseElement, Link


class ModalCart:
    """
    PageComponent ModalCart
    Modal window with information about the product added to the cart
    """

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "modal_content"

        self.__modal_title = BaseElement(
            self.browser,
            name="modal_content_title",
            locator=(By.CSS_SELECTOR, f"div.modal-title"),
        )
        self.__modal_item_cart = BaseElement(
            self.browser,
            name="modal_content_item_cart",
            locator=(By.CSS_SELECTOR, f"div.modal-cart-item"))

        self.__modal_item_cart_title = BaseElement(
            self.browser,
            name="modal_content_item_cart_title",
            locator=(By.CSS_SELECTOR, f"a.modal-cart-item__title"))

        self.__modal_item_cart_price = BaseElement(
            self.browser,
            name="modal_content_item_cart_price",
            locator=(By.CSS_SELECTOR, f"span.modal-cart-item__price"))

        self.__link_go_to_cart = Link(
            self.browser,
            name="link_go_to_basket",
            locator=(By.CSS_SELECTOR, "a[class*='btn'][href='/cart/']"))

    @property
    def product_id(self) -> str:
        """Returns: product id in modal item cart"""
        product_id = self.__modal_item_cart.get_element().get_attribute("data-id")
        logger.info(f"Get product id - {product_id}")
        return product_id

    @property
    def product_name(self) -> str:
        """Returns: product name in modal item cart"""
        product_name = self.__modal_item_cart_title.get_element().text
        logger.info(f"Get product name - {product_name}")
        return product_name

    @property
    def product_price(self) -> str:
        """Returns: product price in modal item cart"""
        product_price = self.__modal_item_cart_price.get_element().text
        logger.info(f"Get product price - {product_price}")
        return product_price

    def go_to_checkout_page(self) -> CheckoutPage:
        """Goes to CheckoutPage"""
        logger.info(f"Go to checkout page")
        self.__link_go_to_cart.get_element().click()
        return CheckoutPage(self.browser)
