def test_class_product_init(test_product1):
    assert test_product1.name == "Арбуз"
    assert test_product1.description == "Свежий"
    assert test_product1.price == 85
    assert test_product1.quantity == 8


def test_new_product(test_product2):
    assert test_product2.name == "Груша"
    assert test_product2.description == "Похожа на яблоко которое начало принимать форму капли"
    assert test_product2.price == 99
    assert test_product2.quantity == 7


def test_new_price(test_product2):
    test_product2.price = 800
    assert test_product2.price == 800
    test_product2.price = -100
    assert test_product2.price == 800
    test_product2.price = 0
    assert test_product2.price == 800



