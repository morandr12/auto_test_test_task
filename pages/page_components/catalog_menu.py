"""The module contains PageComponent CatalogMenu"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from loguru import logger
from pages.page_elements.elements import Link
from data.catalogs import Catalog


class CatalogMenu:
    """
    PageComponent CatalogMenu
    Dropdown menu with catalogs
    """

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "Dropdown catalog menu"

    def open_catalog_page_from_menu_by_path(self, *catalog_path: Catalog):
        """
        Open a catalog page by navigating through the menu at a given path to catalog.
        Parameters: *catalog_path
        """
        logger.info(
            f"Open a catalog page by navigating through the menu, path {[catalog.name for catalog in catalog_path]}"
        )
        for catalog_index, catalog in enumerate(catalog_path, start=1):
            link = Link(self.browser, name=catalog.name, locator=(By.CSS_SELECTOR, f"a[href='/{catalog.link}'"))
            if catalog_index < len(catalog_path):
                link.move_to_link()
            else:
                link.click_to_element()
