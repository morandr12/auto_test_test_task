"""The module contains PageObject BasePage"""

from loguru import logger
from selenium import webdriver


class BasePage:
    """PageObject BasePage"""

    def __init__(self, browser: webdriver, url: str):
        self.browser = browser
        self.url = url

    @property
    def current_url(self) -> str:
        """Get current URL"""
        current_url = self.browser.current_url
        logger.info(f"Get current page url {current_url}")
        return current_url

    def open(self):
        """Open page"""
        self.browser.get(self.url)
        logger.info(f"Open page {self.url}")
        return self
