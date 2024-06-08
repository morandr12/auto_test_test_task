"""The module contains users dataclasses"""

from dataclasses import dataclass


@dataclass
class User:
    """Dataclass for users"""

    name: str
    midname: str
    surname: str
    email: str
    phone: str
    password: str


user_tester = User(
    name="Виктор",
    midname="Петрович",
    surname="Сидоров",
    email="tester12@example.com",
    phone="+799911155588",
    password="qwerty@1",
)
