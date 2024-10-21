from src.class_category import Category
from src.class_product import Product


class Iterator:
    object: Category

    def __init__(self, object_class):
        self.object = object_class

    def __iter__(self):
        return self

    def __next__(self):
        for product in object.products:
            return product


if __name__ == '__main__':
    prod1 = Product("Арбуз", "Свежий", 85, 8)
    cat1 = Category("Ягоды",
                    "Арбуз - это тоже ягода",
                    [])
    cat1.products = prod1

    it = Iterator(cat1)

    print(list(it))
