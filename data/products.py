from dataclasses import dataclass


@dataclass
class Product:
    name: str
    id: str
    link: str
    price: str


planshet_digma = Product(
    name="Планшет Digma iDx10 8Gb",
    id="53",
    link="product/Planshet-Digma-iDx10-8Gb/",
    price="9 680",
)
