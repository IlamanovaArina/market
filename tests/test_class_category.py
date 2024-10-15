def test_product_init(test_category):
    assert test_category.name == "Ягоды"
    assert test_category.description == "Арбуз - это тоже ягода"
    assert len(test_category.products) == 1
    assert test_category.category_count == 1
    assert test_category.product_count == 8
