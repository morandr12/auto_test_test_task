"""The module contains PageComponent LoginModal"""

from loguru import logger

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.elements.elements import BaseElement, InputField, Button


class LoginModal:
    """
    PageComponent LoginModal
    Modal login form
    """

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "modal_login_form"

        self.__modal_title = BaseElement(
            self.browser,
            name="modal_title",
            locator=(By.CSS_SELECTOR, "div.modal-title"),
        )

        self.__input_field_login = InputField(
            self.browser,
            name="input_field_login ",
            locator=(By.CSS_SELECTOR, "input[name='login'"),
        )

        self.__input_field_password = InputField(
            self.browser,
            name="input_field_login ",
            locator=(By.CSS_SELECTOR, "input[name='pass'"),
        )

        self.__login_submit_button = Button(
            self.browser,
            name="input_field_login ",
            locator=(By.CSS_SELECTOR, "form[action='/auth/'] button[type='submit']"),
        )

        self._invalid_login_message = BaseElement(
            self.browser,
            name="invalid_login_message",
            locator=(By.CSS_SELECTOR, ".invalid-feedback"),
        )

    def input_login(self, text: str):
        """
        Input text in login field
        Parameters: text
        Returns: self
        """
        self.__input_field_login.input_text(text)
        return self

    def input_password(self, text: str):
        """
        Input text in password field
        Parameters: text
        Returns: self
        """
        self.__input_field_password.input_text(text)
        return self

    def clear_login_data(self):
        """
        Clear login data in login and password field
        Returns: self
        """
        logger.info("Clear login data")
        self.__input_field_login.clear_text()
        self.__input_field_password.clear_text()
        return self

    def input_login_data(self, email: str, password: str):
        """
        Input user data to login and password field
        Parameters: email: str, password: str
        Returns: self
        """
        self.clear_login_data()
        logger.info(f"Input login data. email {email}, password {password}")
        self.__input_field_login.input_text(email)
        self.__input_field_password.input_text(password)
        return self

    def click_submit_button(self):
        """
        Click to submit button
        Parameters: text
        Returns: self
        """
        logger.info("Click to login submit button")
        self.__login_submit_button.click_to_button()
        return self

    def is_there_invalid_feedback(self) -> bool:
        """
        Check is the invalid feedback about login
        Returns: True/False
        """
        is_there_invalid_feedback = self._invalid_login_message.is_element_present()
        logger.info(
            f"Check is there invalid feedback about login. Result = {is_there_invalid_feedback}"
        )
        return is_there_invalid_feedback
