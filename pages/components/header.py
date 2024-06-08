"""The module contains PageComponents Header, HeadDropdownCatalog, HeadSearchBar"""

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.components.login_modal import LoginModal
from pages.elements.elements import Link, Button, InputField
from data.catalogs import Catalog


class HeadBar:
    """PageComponent HeadBar"""

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "Headbar"

        self.__login_link = Link(
            browser,
            name="login_link",
            locator=(By.CSS_SELECTOR, "a[class='head-bar__link'][href='#'] > span"),
        )
        self.__login_button = Link(
            browser,
            name="login_button_in_dropdown_menu",
            locator=(
                By.CSS_SELECTOR,
                "ul.head-bar__dropdown a[class*='dropdown-item'][href*='/auth/']",
            ),
        )
        self.__user_link = Link(
            browser,
            name="login_link",
            locator=(By.CSS_SELECTOR, "a[class='head-bar__link'][href='/my/'] > span"),
        )
        self.__user_profile_button = Link(
            browser,
            name="user_profile_in_dropdown_menu",
            locator=(By.CSS_SELECTOR, "a[class*='aside-menu__link'][href='/my/']"),
        )

    def open_login_modal(self) -> LoginModal:
        """
        Open login modal form
        Returns: LoginModal
        """
        logger.info("Open login modal form")
        self.__login_link.click_to_element()
        self.__login_button.click_to_element()
        return LoginModal(self.browser)

    def is_user_link_present(self) -> bool:
        """
        Check is user link present
        Returns: text
        """
        is_user_link_present = self.__user_link.is_element_present()
        logger.info(f"Check is user link present. Result = {is_user_link_present}")
        return is_user_link_present

    def get_text_from_user_link(self) -> str:
        """
        Get text from login link
        Returns: text
        """
        text_from_user_link = self.__user_link.get_element().text
        logger.info(f"Get text from user link. Text = {text_from_user_link}")
        return self.__user_link.get_element().text

    def go_to_user_profile_page(self):
        """
        Open User profile page
        """
        logger.info("Open user profile page")
        self.__user_link.click_to_element()
        self.__user_profile_button.click_to_element()


class HeadDropdownCatalog:
    """
    PageComponent HeadDropdownCatalog
    Dropdown menu with catalogs
    """

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "Dropdown catalog menu"

    def open_catalog_page_by_path(self, *catalog_path: Catalog):
        """
        Open a catalog page by navigating through the menu at a given path to catalog.
        Parameters: *catalog_path
        """
        logger.info(
            f"Open a catalog page in menu, path {[catalog.name for catalog in catalog_path]}"
        )
        for catalog_index, catalog in enumerate(catalog_path, start=1):
            link = Link(
                self.browser,
                name=catalog.name,
                locator=(By.CSS_SELECTOR, f"a[href='{catalog.link}'"),
            )
            if catalog_index < len(catalog_path):
                link.move_to_link()
            else:
                link.click_to_element()


class HeadSearchBar:
    """PageComponent HeadSearchBar"""

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "searchbar"

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
        logger.info("Click on submit button in search bar")
        self.__submit_button.click_to_button()
        return self


class Header:
    """PageComponent Header"""

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "Header"

        self.__head_bar = HeadBar(browser)
        self.__search_bar = HeadSearchBar(browser)
        self.__catalog_menu = HeadDropdownCatalog(browser)

        self.__button_catalog = Button(
            browser, name="button_catalog", locator=(By.CSS_SELECTOR, ".head-catalog-btn")
        )

    @property
    def head_bar(self) -> HeadBar:
        """Returns: HeadBar"""
        return self.__head_bar

    @property
    def search_bar(self) -> HeadSearchBar:
        """Returns: HeadSearchBar"""
        return self.__search_bar

    def open_catalog_menu(self) -> HeadDropdownCatalog:
        """Returns: HeadDropdownCatalog"""
        logger.info("Open catalog menu")
        self.__button_catalog.click_to_button()
        return self.__catalog_menu
