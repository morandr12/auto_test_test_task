"""The module contains catalogs dataclasses"""

from dataclasses import dataclass
from data.products import Product, tablet_digma


@dataclass
class Catalog:
    name: str
    ids: str
    link: str
    products_list: list[Product,] | None


electronics = Catalog(
    name="Электроника",
    ids="Catalog Electronics",
    link="/catalog/elektronika/",
    products_list=[tablet_digma],
)

tablets = Catalog(
    name="Планшеты",
    ids="Catalog Tablets",
    link="/catalog/planshety/",
    products_list=[tablet_digma],
)

digma = Catalog(
    name="Digma",
    ids="Catalog Digma",
    link="/catalog/digma/",
    products_list=[tablet_digma],
)
