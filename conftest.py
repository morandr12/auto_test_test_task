import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.page_objects.main_page import MainPage
from pages.page_objects.catalog_page import CatalogPage
from data.pages_links import MAIN_PAGE_LINK


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode.")


@pytest.fixture(scope="function")
def browser(request) -> webdriver:
    options = Options()

    if request.config.getoption("headless"):
        options.add_argument("--headless")

    print("\nstart browser for test..")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver

    print("\nquit browser..")
    driver.quit()


@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def catalog_page(browser, request):
    marker = request.node.get_closest_marker('catalog')
    page_link = None if marker is None else MAIN_PAGE_LINK + marker.args[0]
    return CatalogPage(browser, page_link)

