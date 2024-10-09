class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # def


a = Product("Арбуз", "Спелый", 100.0, 3)
print(a.name)
print(a.description)
print(a.price)
print(a.quantity)