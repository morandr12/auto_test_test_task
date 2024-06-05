from dataclasses import dataclass
from data.products import Product, planshet_digma


@dataclass
class Catalog:
    name: str
    link: str
    products_list: list[Product,] | None


elektroinka = Catalog(name="Электроника", link="catalog/elektronika/", products_list=[planshet_digma])

planshety = Catalog(name="Планшеты", link="catalog/planshety/", products_list=[planshet_digma])

digma = Catalog(name="Digma", link="catalog/digma/", products_list=[planshet_digma])

