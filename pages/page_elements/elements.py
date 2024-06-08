"""The module contains Page Elements"""

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, browser: webdriver, name: str, locator: tuple[str, str]):
        self.browser = browser
        self.name = name
        self.locator = locator

    def is_element_present(self, timeout: float = 4, *arg, **kwargs):
        """Проверка отсутствия локатора элемента."""
        try:
            WebDriverWait(self.browser, timeout, *arg, **kwargs).until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            return False
        return True

    def get_element(self, timeout: float = 4, *arg, **kwargs) -> WebElement:
        """
        Get element
        Parameters: timeout - timeout to wait when element to be located and visibility
        Returns: WebElement
        """
        return WebDriverWait(self.browser, timeout, *arg, **kwargs).until(
            EC.visibility_of_element_located(self.locator),
            message=f"Can't find element {self.name} by locator {self.locator}",
        )

    def get_all_elements(self, timeout: float = 4, *arg, **kwargs) -> list[WebElement]:
        """
        Get all (list) elements
        Returns: list[WebElement]
        """
        return WebDriverWait(self.browser, timeout, *arg, **kwargs).until(
            EC.presence_of_all_elements_located(self.locator),
            message=f"Can't find any elements {self.name} by locator {self.locator}",
        )


class ClickableElement(BaseElement):

    def click_to_element(self, timeout: float = 4, *arg, **kwargs):
        """
        Click to element
        Parameters: timeout - timeout to wait when element to be clickable
        Returns: None
        """
        element = WebDriverWait(self.browser, timeout, *arg, **kwargs).until(
            EC.element_to_be_clickable(self.locator),
            message=f"Element {self.name} by locator {self.locator} is not clickable",
        )
        element.click()


class Button(ClickableElement):
    def click_to_button(self, timeout: float = 4, *arg, **kwargs):
        """
        Click to button
        Parameters: timeout - timeout to wait when element to be clickable
        Returns: None
        """
        self.click_to_element(timeout, *arg, *kwargs)


class Link(ClickableElement):
    def move_to_link(self, timeout: float = 4, *arg, **kwargs):
        """
        Move(hover) mouse cursor to link
        Parameters: timeout - timeout to wait when element to be located and visibility
        Returns: None
        """
        element = self.get_element(timeout=timeout, *arg, **kwargs)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()


class InputField(BaseElement):
    """
    Input text to Input field
    Parameters:
        text - text to input
        timeout - timeout to wait when element to be located and visibility
    Returns: None
    """

    def input_text(self, text: str, timeout: float = 4, *arg, **kwargs):
        element = self.get_element(timeout=timeout, *arg, **kwargs)
        element.send_keys(text)
