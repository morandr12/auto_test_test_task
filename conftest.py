import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.page_objects.main_page import MainPage
from pages.page_objects.catalog_page import CatalogPage
from pages.page_objects.checkout_page import CheckoutPage
from pages.page_objects.user_profile_page import UserProfilePage
from data.pages_links import MAIN_PAGE_LINK, RESULT_QUERY_LINK
from utilits.logger import logger


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Run browser in headed mode.")


@pytest.fixture(scope="function")
def browser(request) -> webdriver:
    options = Options()

    if not request.config.getoption("headed"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    logger.info("Start browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1920, 1080)

    yield browser

    logger.info("Quit browser..")
    browser.quit()


@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def user_profile_page(browser):
    return UserProfilePage(browser)


@pytest.fixture()
def checkout_page(browser):
    return CheckoutPage(browser)


@pytest.fixture()
def catalog_page(browser, request):
    page_link = MAIN_PAGE_LINK + request.param.link
    return CatalogPage(browser, page_link)


@pytest.fixture()
def result_query_page(browser):
    return CatalogPage(browser, url=RESULT_QUERY_LINK)
