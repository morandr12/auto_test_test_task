from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.page_elements.elements import Input, Button, Link


class SearchBarComponent:
    """PageComponent SearchBar"""

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.name = "Dropdown catalog menu"
        self.__input_form = Input(
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
        self.__input_form.input_text(text)

    def submit_button_click(self):
        self.__submit_button.click_to_button()

    def select_dropdown_item_by_index(self, list_index: str, item_index: str):
        dropdown_item = Link(
            self.browser,
            name="dropdown_item",
            locator=(
                By.CSS_SELECTOR,
                f".head-search__dropdown > #autoComplete_list_{list_index} > #autoComplete_result_{item_index} > a",
            ),
        )
        dropdown_item.move_to_link()
        dropdown_item.click_to_element()
