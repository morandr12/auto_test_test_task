import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.page_objects.main_page import MainPage
from pages.page_objects.catalog_page import CatalogPage
from data.pages_links import MAIN_PAGE_LINK, RESULT_QUERY_LINK
from utilits.logger import logger


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode.")


@pytest.fixture(scope="function")
def browser(request) -> webdriver:
    options = Options()

    if request.config.getoption("headless"):
        options.add_argument("--headless")

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
def catalog_page(browser, request):
    page_link = MAIN_PAGE_LINK + request.param.link
    return CatalogPage(browser, page_link)


@pytest.fixture()
def result_query_page(browser):
    return CatalogPage(browser, url=RESULT_QUERY_LINK)

