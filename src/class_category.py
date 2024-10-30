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
        """ Добавляет новый продукт в категорию """
        if isinstance(new_product, Product):
            self.__products.append(new_product)

            # Добавляем количество товаров от нового продукта к основному количеству
            Category.product_count += new_product.quantity
        else:
            raise TypeError

    @property
    def products(self):
        """ Даёт доступ для просмотра списка товаров (объекты) """
        return self.__products

    @products.setter
    def products(self, prod):
        """ Добавляет (объект) продукт в список товаров """
        self.__products.append(prod)
        Category.product_count += prod.quantity

    def __str__(self):
        """ Выводит в виде строки данные о товаре """
        str_product = ""
        for prod in self.__products:
            str_product += f"{prod.name}, количество продуктов: {prod.quantity} шт.\n"
        return str_product

    def __len__(self):
        """ Показывает сколько (объектов) продуктов в списке продуктов """
        for prod in self.__products:
            return len(prod.products)

    def middle_price(self):
        """ Средняя цена продуктов данной категории """
        try:
            len_ = 0
            price_ = 0

            for prod in self.__products:
                price_ += prod.price
                len_ = len(self.products)
            if len_ > 0:
                result = price_ / len_
                return round(result, 1)
            elif price_ <= 0:
                return 0
            else:
                return 0
        except Exception as e:
            return f"Возбуждено исключение: {e}"
