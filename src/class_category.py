from itertools import product

from src.class_product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
        Category.product_count += len(product)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self):
        self.__products.append(product)
        self.product_count += 1



