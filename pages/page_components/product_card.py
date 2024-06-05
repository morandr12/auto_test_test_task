from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.page_elements.elements import BaseElement, Button, Link


class ProductCard:
    """PageComponent ProductCard"""

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
            name="item-product-price__new-price",
            locator=(By.CSS_SELECTOR, f"div[data-id='{self.product_id}'] div.item-product-price__new-price > span"),
        )
        self.__button_add_to_basket = Button(
            self.browser,
            name="button_add_item_to_basket",
            locator=(By.CSS_SELECTOR, f"div[data-id='{self.product_id}'] div.item-product-cart-action > button"),
        )

    @property
    def product_name(self):
        return self.__product_title.get_element().text

    @property
    def product_link(self):
        return self.__product_title.get_element().get_attribute("href")

    @property
    def product_price(self):
        return self.__product_price.get_element().text

    @property
    def product_img_alt(self):
        return self.__product_img.get_element().get_attribute("alt")

    def find_product_card(self):
        try:
            self.__data_id.get_element()
        except NoSuchElementException:
            return False
        return True
