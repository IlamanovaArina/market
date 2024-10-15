import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def test_product1():
    return Product("Арбуз", "Свежий", 85,8)


@pytest.fixture
def test_product2():
    return Product.new_product(
        {"name": "Груша",
         "description": "Похожа на яблоко которое начало принимать форму капли",
         "price": 99,
         "quantity": 7})


@pytest.fixture
def test_category1():
    return Category("Ягоды",
                    "Арбуз - это тоже ягода",
                    [])


