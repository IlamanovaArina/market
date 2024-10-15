import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def test_product():
    return Product("Арбуз", "Свежий", 85,8)


@pytest.fixture
def test_category():
    test_product = Product("Арбуз", "Свежий", 85, 8)
    return Category("Ягоды",
                    "Арбуз - это тоже ягода", [test_product])
