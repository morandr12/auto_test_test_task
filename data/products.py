"""The module contains products dataclasses"""

from dataclasses import dataclass


@dataclass
class Product:
    """Dataclass for products"""
    id: str
    name: str
    ids: str
    manufacture: str
    link: str
    price: str


tablet_digma = Product(
    id="53",
    name="Планшет Digma iDx10 8Gb",
    ids="Tablet Digma iDx10 8Gb",
    manufacture="Digma",
    link="/product/Planshet-Digma-iDx10-8Gb/",
    price="9 680",
)
