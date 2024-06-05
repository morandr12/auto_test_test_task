import pytest

from loguru import logger

from pages.page_objects.main_page import MainPage
from pages.page_objects.catalog_page import CatalogPage
from data.catalogs import elektroinka, planshety, digma
from data.products import planshet_digma


@pytest.mark.catalog(digma.link)
class TestSuiteCatalogDigma:

    catalog_path = (elektroinka, planshety, digma)
    products = [planshet_digma]

    def test_open_catalog_page_from_catalog_menu(
        self,
        main_page: MainPage,
        catalog_page: CatalogPage,
    ):
        main_page.open().open_catalog_menu().open_catalog_page_from_menu_by_path(*self.catalog_path)

        assert catalog_page.current_url == main_page.url + self.catalog_path[-1].link
        assert catalog_page.catalog_name == self.catalog_path[-1].name
        assert catalog_page.category_names_path == ["Главная"] + [catalog.name for catalog in self.catalog_path]

    def test_search_and_open_result_page_from_search_bar(
        self,
        main_page: MainPage,
        catalog_page: CatalogPage,
        search_query=digma.name
    ):
        main_page.open().perform_search_query(search_query)

        assert catalog_page.current_url == main_page.url + f"catalog/all/?query={search_query}"
        assert catalog_page.catalog_name == "Результаты поиска"
        assert catalog_page.category_names_path == ["Главная", "Результаты поиска"]

    def test_search_and_open_catalog_page_from_search_bar(
        self,
        main_page: MainPage,
        catalog_page: CatalogPage,
        search_query=digma.name
    ):
        main_page.open().select_by_search_query(search_query, list_index=1, item_index=1)

        assert catalog_page.current_url == main_page.url + self.catalog_path[-1].link
        assert catalog_page.catalog_name == search_query
        assert catalog_page.category_names_path == ["Главная"] + [catalog.name for catalog in self.catalog_path]

    @pytest.mark.parametrize("product", products)
    def test_product_in_catalog_page(self, catalog_page: CatalogPage, product: planshet_digma):

        catalog_page.open()

        if not catalog_page.is_there_product_in_catalog(product.id):
            pytest.fail(f"Can't find {product.name} with id {product.id} in catalog {catalog_page.current_url}")

        product_card = catalog_page.get_product_card_by_id(product.id)

        assert product_card.product_name == product.name
        assert product_card.product_link == MainPage.url + product.link
        assert product_card.product_img_alt == product.name
        assert product_card.product_price == product.price
