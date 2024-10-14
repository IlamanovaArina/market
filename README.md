# Маркет

Мы создаём ядро для интернет-магазина


## Функционал

У нас есть несколько классов:


### Класс `Product`
Помогает создавать объекты из данных 
о товаре, который мы предоставляем.
У него есть такие атрибуты: 
```  
class Product:  
    name: str
    description: str
    price: float
    quantity: int
```
где `name` - название товара,
`description` - его описание,
`price` - цена,
`quantity` - количество в наличии.


### Класс `Category`
Показывает категокии товаров, их количество и количество товаров

``` 
class Category:
    name: str
    description: str
    products: list
```
`name` - название категории,
`description` - описание,
`products` - список товаров категории,
`category_count` - количество категорий, 
`product_count` - количество товаров.

## 
