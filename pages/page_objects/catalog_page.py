"""The module contains PageObject CatalogPage"""

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_objects.main_page import MainPage
from pages.page_elements.elements import BaseElement
from pages.page_components.product_card import ProductCard


class CatalogPage(MainPage):
    """Class PageObject CatalogPage"""

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
        """Return: current catalog name from catalog page"""
        catalog_name = self.__header_with_catalog_name.get_element().text
        logger.info(f"Get current catalog name from catalog page - {catalog_name}")
        return catalog_name

    @property
    def category_names_path(self) -> list[str]:
        """Return: current category names path from catalog page"""
        category_names_path = [item.text for item in self.__breadcrumb_item.get_all_elements()]
        logger.info(f"Get current category names path from catalog page - {category_names_path}")
        return category_names_path

    def is_there_product_in_catalog(self, product_id: str) -> bool:
        """
        Try to find product card in catalog by id
        Parameters: product_id
        Returns:
            True - if there is product card
            False - if there is no product card
        """
        is_there_product = self.get_product_card_by_id(product_id).is_there_product_card()
        logger.info(f"Search product with id {product_id} in catalog, result = {is_there_product}")
        return is_there_product

    def get_product_card_by_id(self, product_id: str) -> ProductCard:
        """
        Get PageComponent ProductCard by product id
        Parameters: product_id
        Return: PageComponent ProductCard"""
        return ProductCard(self.browser, product_id)
