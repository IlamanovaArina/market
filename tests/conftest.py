import pytest

from src.class_category import Category
from src.class_product import Product
from src.classes_child import Smartphone, LawnGrass


@pytest.fixture
def test_product1():
    return Product("Арбуз", "Свежий", 85, 8)


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


@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5,
                      95.5,
                      "S23 Ultra",
                      256,
                      "Серый")


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15",
                      "512GB, Gray space",
                      210000.0,
                      8,
                      98.2,
                      "15",
                      512,
                      "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава",
                     "Элитная трава для газона",
                     500.0,
                     20,
                     "Россия",
                     "7 дней",
                     "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2",
                     "Выносливая трава",
                     450.0,
                     15,
                     "США",
                     "5 дней",
                     "Темно-зеленый")
