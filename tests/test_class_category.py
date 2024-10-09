from unittest.mock import Mock


def test_product_init(test_category):
    assert test_category.name == "Ягоды"
    assert test_category.description == "Арбуз - это тоже ягода"
    assert len(test_category.products) == 1
    assert test_category.category_count == 1
    assert test_category.product_count == 1
    x = Mock(category=["<function test_product at 0x0000025FB55EE8E0>"])
    test_category.products = x
    assert test_category.products == x
