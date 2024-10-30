from src.class_product import Product


def test_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    messege = capsys.readouterr()
    assert messege.out == "Product, (Iphone 15, 512GB, Gray space, 210000.0, 8)\n"
