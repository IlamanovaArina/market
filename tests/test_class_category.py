def test_product_init(test_category1, test_product1):
    test_category1.products = test_product1

    assert test_category1.name == "Ягоды"
    assert test_category1.description == "Арбуз - это тоже ягода"
    assert len(test_category1.products) == 1
    assert test_category1.category_count == 1
    assert test_category1.product_count == 8


def test_product_(test_category1, test_product2):
    test_category1.add_product(test_product2)

    assert test_category1.name == "Ягоды"
    assert test_category1.description == "Арбуз - это тоже ягода"
    assert len(test_category1.products) == 1
    assert test_category1.category_count == 2
    assert test_category1.product_count == 15
