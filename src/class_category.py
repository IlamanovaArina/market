from src.class_product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        for p in products:
            Category.product_count += p.quantity

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += new_product.quantity

    @property
    def products(self):
        str_product = ""
        for prod in self.__products:
            str_product += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return str_product

    @products.setter
    def products(self, prod):
        self.__products.append(prod)
        Category.product_count += prod.quantity

    def __str__(self):
        str_product = ""
        for prod in self.__products:
            str_product += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return str_product