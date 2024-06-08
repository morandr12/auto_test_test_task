"""The module contains Test Suites Product"""

import pytest
import pytest_check
from loguru import logger

from pages.page_objects.main_page import MainPage
from pages.page_objects.catalog_page import CatalogPage
from pages.page_objects.checkout_page import CheckoutPage
from data.catalogs import electronics, tablets, digma
from data.products import tablet_digma
from data.pages_links import RESULT_QUERY_LINK


class TestSuiteProduct:

    digma_catalog_path = [electronics, tablets, digma]
    digma_catalog = digma_catalog_path[-1]
    product = tablet_digma

    @pytest.mark.parametrize(
        "catalog_page, catalog_path",
        [(digma_catalog, digma_catalog_path)],
        ids=[digma_catalog.ids],
        indirect=["catalog_page"],
    )
    def test_open_catalog_page_from_catalog_menu(
        self, main_page: MainPage, catalog_page: CatalogPage, catalog_path
    ):
        """Test of opening a catalog page from the catalog drop-down menu on the main page"""

        logger.info("Start test_open_catalog_page_from_catalog_menu")

        main_page.open()

        # chain of actions to open a catalog page
        main_page.header.open_catalog_menu().open_catalog_page_by_path(*catalog_path)

        # soft asserts with pytest_check
        logger.info("Check current page url")
        pytest_check.equal(
            catalog_page.current_url,
            main_page.url + catalog_path[-1].link,
            msg="Current page url doesn't equal expected url",
        )
        logger.info("Check current catalog name")
        pytest_check.equal(
            catalog_page.catalog_name,
            catalog_path[-1].name,
            msg="Current catalog name doesn't equal expected catalog name",
        )
        logger.info("Check current category names path")
        pytest_check.equal(
            catalog_page.category_names_path,
            ["Главная"] + [catalog.name for catalog in catalog_path],
            msg="Current category path doesn't equal expected catalog category path",
        )

    @pytest.mark.parametrize(
        "catalog_page, product",
        [(digma_catalog, product)],
        ids=[product.ids],
        indirect=["catalog_page"],
    )
    def test_product_in_catalog_page(self, catalog_page: CatalogPage, product):
        """Test product on catalog page"""

        logger.info("Start test_product_in_catalog_page")

        catalog_page.open()

        logger.info("Assert is there product in catalog")
        assert catalog_page.is_there_product_in_catalog(
            product.id
        ), f"There is not {product.name} with id {product.id} in catalog {catalog_page.current_url}"

        product_card = catalog_page.get_product_card_by_id(product.id)

        # soft asserts with pytest_check
        logger.info("Check current product name")
        pytest_check.equal(
            product_card.product_name,
            product.name,
            msg="Current product name doesn't equal expected product name",
        )
        logger.info("Check current product link")
        pytest_check.equal(
            product_card.product_link,
            MainPage.url + product.link,
            msg="Current product link  doesn't equal expected product link",
        )
        logger.info("Check current product price")
        pytest_check.equal(
            product_card.product_price,
            product.price,
            msg="Current product price  doesn't equal expected product price",
        )

    @pytest.mark.parametrize(
        "catalog_page, product",
        [(digma_catalog, product)],
        ids=[product.ids],
        indirect=["catalog_page"],
    )
    def test_add_delete_products_to_cart(
        self, catalog_page: CatalogPage, checkout_page: CheckoutPage, product
    ):
        """Test adding and deleting product to cart"""

        logger.info("Start test_add_delete_products_to_cart")

        catalog_page.open()

        # chain of actions for adding product to the cart and obtaining a modal form of the added product
        cart_modal = catalog_page.get_product_card_by_id(product.id).add_product_to_cart()

        # soft assert with pytest_check
        logger.info("Check current product id ")
        pytest_check.equal(
            cart_modal.product_id,
            product.id,
            msg="Current product id doesn't equal expected product id",
        )
        logger.info("Check current product name")
        pytest_check.equal(
            cart_modal.product_name,
            product.name,
            msg="Current product name doesn't equal expected product name",
        )

        cart_modal.go_to_checkout_page()

        logger.info("Assert is there product in cart")
        assert (
            checkout_page.cart.is_there_product_in_cart(product.id) is True
        ), f"There is not {product.name} with id {product.id} in cart"

        # deleting product from the cart
        checkout_page.cart.delete_product(product.id)

        checkout_page.open()

        logger.info("Assert is not there product in cart")
        assert (
            checkout_page.cart.is_there_product_in_cart(product.id) is False
        ), f"There is {product.name} with id {product.id} in cart"

    @pytest.mark.parametrize(
        "query",
        [
            pytest.param(
                electronics,
                marks=pytest.mark.xfail(reason="Maybe it's a bug, nothing found by query"),
            ),
            tablets,
            digma,
            tablet_digma,
        ],
        ids=[electronics.ids, tablets.ids, digma.ids, tablet_digma.ids],
    )
    def test_search_product_for_query_in_search_bar(
        self, main_page: MainPage, result_query_page: CatalogPage, query
    ):
        """Test searching product for a query in the search bar"""
        logger.info("Start test_search_product_for_query_in_search_bar")

        main_page.open()

        # chain of actions for executing a query in the search bar
        main_page.header.search_bar.input_text(query.name).click_submit_button()

        logger.info("Check is this result query page")
        pytest_check.is_in(
            RESULT_QUERY_LINK,
            result_query_page.current_url,
            "Current page url doesn't equal expected url",
        )

        logger.info("Assert is there product in result query page")
        assert (
            result_query_page.is_there_product_in_catalog(tablet_digma.id) is True
        ), f"There is not {tablet_digma.name} with id {tablet_digma.id} in result"
