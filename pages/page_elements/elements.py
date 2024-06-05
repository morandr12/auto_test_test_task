import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, browser: webdriver, name: str, locator: tuple[str, str]):
        self.browser = browser
        self.name = name
        self.locator = locator

    def get_element(self, timeout: float = 5, *arg, **kwargs) -> WebElement:
        """Получить элемент"""
        return WebDriverWait(self.browser, timeout, *arg, **kwargs).until(
            EC.presence_of_element_located(self.locator),
            message=f"Can't find element {self.name} by locator {self.locator}",
        )


    def get_all_elements(self, timeout: float = 5, *arg, **kwargs) -> list[WebElement]:
        """Получить список элементов страницы"""
        return WebDriverWait(self.browser, timeout, *arg, **kwargs).until(
            EC.presence_of_all_elements_located(self.locator)
        )


class ClickableElement(BaseElement):

    def click_to_element(self, timeout: float = 5, *arg, **kwargs) -> None:
        """Кликнуть по элементу"""
        element = WebDriverWait(self.browser, timeout, *arg, **kwargs).until(
            EC.element_to_be_clickable(self.locator),
            message=f"Element {self.name} by locator {self.locator} is not clickable",
        )
        element.click()


class Button(ClickableElement):
    def click_to_button(self, timeout: float = 5, *arg, **kwargs) -> None:
        self.click_to_element(timeout, *arg, *kwargs)


class Link(ClickableElement):
    def move_to_link(self, timeout: float = 5, *arg, **kwargs):
        element = WebDriverWait(self.browser, timeout, *arg, **kwargs).until(
            EC.visibility_of_element_located(self.locator),
            message=f"Element {self.name} by locator {self.locator} is not visibility",
        )
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()


class Input(BaseElement):
    def input_text(self, text: str, timeout: float = 5, *arg, **kwargs):
        element = WebDriverWait(self.browser, timeout, *arg, **kwargs).until(
            EC.visibility_of_element_located(self.locator),
            message=f"Element {self.name} by locator {self.locator} is not visibility",
        )
        element.send_keys(text)
