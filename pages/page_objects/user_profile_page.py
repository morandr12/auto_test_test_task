"""The module contains PageObject UserProfilePage"""

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.page_objects.base_page import BasePage
from pages.components.header import Header
from pages.elements.elements import InputField
from data.pages_links import MAIN_PAGE_LINK


class UserProfilePage(BasePage):
    """PageObject UserProfilePage"""

    url = MAIN_PAGE_LINK

    def __init__(self, browser: webdriver, url: str = url):
        super().__init__(browser, url)
        self.__header = Header(browser)

        self.__name_filed = InputField(
            browser,
            name="name_filed",
            locator=(By.CSS_SELECTOR, "input[name='name']"),
        )
        self.__surename_filed = InputField(
            browser,
            name="surename_filed",
            locator=(By.CSS_SELECTOR, "input[name='surname']"),
        )
        self.__phone_filed = InputField(
            browser,
            name="phone_filed",
            locator=(By.CSS_SELECTOR, "input[name='phone']"),
        )
        self.__email_filed = InputField(
            browser,
            name="email_filed",
            locator=(By.CSS_SELECTOR, "input[name='e_mail']"),
        )

    @property
    def header(self) -> Header:
        """Return: Header"""
        return self.__header

    @property
    def user_name(self) -> str:
        """Returns: user name"""
        user_name = self.__name_filed.get_element().get_attribute("value")
        logger.info(f"Get user name - {user_name}")
        return user_name

    @property
    def user_surename(self) -> str:
        """Returns: user surename"""
        user_surename = self.__surename_filed.get_element().get_attribute("value")
        logger.info(f"Get user surename - {user_surename}")
        return user_surename

    @property
    def user_phone(self) -> str:
        """Returns: user phone"""
        user_phone = self.__phone_filed.get_element().get_attribute("value")
        logger.info(f"Get user phone - {user_phone}")
        return user_phone

    @property
    def user_email(self) -> str:
        """Returns: user emial"""
        user_email = self.__email_filed.get_element().get_attribute("value")
        logger.info(f"Get user email - {user_email}")
        return user_email
