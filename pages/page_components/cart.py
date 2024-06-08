"""The module contains PageComponent Cart"""

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from pages.page_elements.elements import BaseElement, Button


class Cart:
    """
    PageComponent Cart
    Card with products on the CheckoutPage
    """

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "Cart"

    def is_there_product_in_cart(self, product_id: str) -> bool:
        """
        Try to find product in cart
        Parameters: product_id
        Returns:
            True - if there is product card
            False - if there is no product card
        """
        return BaseElement(
            self.browser,
            name="product_card_in_cart",
            locator=(By.CSS_SELECTOR, f"div[class*='cart-checkout-item'][data-id='{product_id}']"),
        ).is_element_present()

    def delete_product(self, product_id: str):
        """
        Click  button delete product in cart by product id.
        Parameters: product_id
        Returns: None
        """
        Button(
            self.browser,
            name="button_delete_product_from_cart",
            locator=(By.CSS_SELECTOR, f"div[class*='cart-checkout-item'][data-id='{product_id}'] a.rs-remove"),
        ).click_to_button()
