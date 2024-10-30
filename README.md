# Маркет

Мы создаём ядро для интернет-магазина
Созданы несколько классов для хранения информации про 
имеющиеся товары и их категории


## Функционал

### Базовый и Миксин-классы

У нас есть базовый абстрактный класс:

```
class BaseProduct(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
```

И Миксин-класс, который выводит:
"Класс('Продукт1', 'Описание продукта', стоимость, количество)"


У нас есть несколько классов:

### Класс `Product`
Помогает создавать объекты из данных 
о товаре, который мы предоставляем.
У него есть такие атрибуты: 
```  
class Product:  
    name: str
    description: str
    __price: float
    quantity: int
```
где `name` - название товара,
`description` - его описание,
`price` - цена,
`quantity` - количество в наличии.

Его методы:

```new_product
    @classmethod
    def new_product(cls, my_dict):
        """ Метод добавляет новые товары из словаря """
        pass
```

```price
    @property
    def price(self):
        """ Даёт доступ для просмотра приватной цены """
        pass
```

```price
    @price.setter
    def price(self, new_price):
        """ Меняет цену если указано число больше 0 """
        pass
```

```__str__
    def __str__(self):
        """ Выводит в виде строки данные о товаре """
        pass
```

```
    def __add__(self, other):
        """ Возвращает стоимость складываемых товаров 
        умноженную на их количество на складе """
        pass
```

```
    def middle_price(self):
        """ Средняя цена продуктов данной категории """
        pass
```


### Класс `Category`
Показывает категокии товаров, их количество и количество товаров

``` 
class Category:
    name: str
    description: str
    products: list
```
где `name` - название категории,
`description` - описание,
`products` - список товаров категории,
`category_count` - количество категорий, 
`product_count` - количество товаров.

Есть методы:

```add_product
    def add_product(self, new_product):
        """ Добавляет новый продукт в категорию """
        pass
```

```products
    @property
    def products(self):
        """ Даёт доступ для просмотра списка товаров (объекты) """
        pass
```

```products
    @products.setter
    def products(self, prod):
        """ Добавляет (объект) продукт в список товаров """
        pass
```

```__str__
    def __str__(self):
        """ Выводит в виде строки данные о товаре """
        pass
```

```__len__
    def __len__(self):
        """ Показывает сколько (объектов) продуктов в списке продуктов """
        pass
```

## 
