"""The module contains PageComponent ProductCard"""

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_elements.elements import BaseElement, Button, Link
from pages.page_components.modal_cart import ModalCart


class ProductCard:
    """
    PageComponent ProductCard
    Product card on the CatalogPage
    """

    def __init__(self, browser: webdriver, product_id: str):
        self.browser = browser
        self.name = "Product_card"
        self.product_id = product_id

        self.__data_id = BaseElement(
            self.browser,
            name="item_card_id",
            locator=(By.CSS_SELECTOR, f"div[data-id='{self.product_id}']"),
        )

        self.__product_title = Link(
            self.browser,
            name="item_card_title",
            locator=(By.CSS_SELECTOR, f"div[data-id='{self.product_id}'] a.item-card__title"),
        )
        self.__product_img = Link(
            self.browser,
            name="item_card_title",
            locator=(By.CSS_SELECTOR, f"div[data-id='{self.product_id}'] a.item-product-img > img"),
        )

        self.__product_price = BaseElement(
            self.browser,
            name="item_product_price",
            locator=(By.CSS_SELECTOR, f"div[data-id='{self.product_id}'] div.item-product-price__new-price > span"),
        )
        self.__button_add_to_cart = Button(
            self.browser,
            name="button_add_item_to_cart",
            locator=(By.CSS_SELECTOR, f"div[data-id='{self.product_id}'] div.item-product-cart-action > button"),
        )

    @property
    def product_name(self) -> str:
        """Returns: product name in product card"""
        product_name = self.__product_title.get_element().text
        logger.info(f"Get product name - {product_name }")
        return product_name

    @property
    def product_link(self) -> str:
        """Returns: product link in product card"""
        product_link = self.__product_title.get_element().get_attribute("href")
        logger.info(f"Get product link - {product_link}")
        return product_link

    @property
    def product_price(self) -> str:
        """Returns: product price in product card"""
        product_price = self.__product_price.get_element().text
        logger.info(f"Get product price - {product_price}")
        return product_price

    def is_there_product_card(self) -> bool:
        """
        Try to find product card
        Returns:
            True - if there is product card
            False - if there is no product card
        """
        return self.__data_id.is_element_present()

    def add_product_to_cart(self):
        """
        Click button add product to cart
        Returns: ModalCart - modal window with information about the added product
        """
        logger.info(f"Add product with id {self.product_id} to cart")
        self.__button_add_to_cart.click_to_button()
        return ModalCart(self.browser)
