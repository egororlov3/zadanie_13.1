class Category:
    """ Класс для предоставления товара в магазине"""

    total_categories = 0
    total_uniques = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Создание экземпляра класса category

        :param name: Название товара
        :param description: Описание товара
        :param products: Товары в магазине"""

        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += len(set([product.name for product in products]))
        Category.total_uniques += 1

    def products(self, product):
        """Принимает товар и добавляет его в список"""
        return self.__products.append(product)

    @property
    def return_products(self):
        """Выводит список товаров"""
        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. остаток:{product.quantity} шт."
        return product_list


class Product:
    """Класс для предоставления кол-во в наличии и цены"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса product

            :param name: Название товара
            :param description: Описание товара
            :param price: Цена за единицу товара
            :param quantity: Количество товара в магазине"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price



