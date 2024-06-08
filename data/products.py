"""The module contains products dataclasses"""

from dataclasses import dataclass


@dataclass
class Product:
    id: str
    name: str
    manufacture: str
    link: str
    price: str


planshet_digma = Product(
    id="53",
    name="Планшет Digma iDx10 8Gb",
    manufacture="Digma",
    link="product/Planshet-Digma-iDx10-8Gb/",
    price="9 680",
)
