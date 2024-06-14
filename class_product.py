from abc import abstractmethod, ABC
from mixin_classes import MixinProd


class Item(ABC):
    """Основной абстрактный класс"""

    @abstractmethod
    def new_product(self, *args, **kwargs):
        """Добавление новых продуктов"""
        pass


class Product(Item, MixinProd):
    """Класс для предоставления кол-во в наличии и цены"""

    def __init__(self, name: str, description: str, color: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса product

            :param name: Название товара
            :param description: Описание товара
            :param color: Цвет товара
            :param price: Цена за единицу товара
            :param quantity: Количество товара в магазине"""

        self.name = name
        self.description = description
        self.color = color
        self.__price = price
        self.quantity = quantity
        print(super().__repr__)

    def __str__(self):
        """Выводит новое строковое отображение"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity}.'

    def __add__(self, other):
        """Считает сумму двух разных продуктов
           в формате цена*количество
           чтобы узнать полную стоимость всех подобных продуктов"""
        if isinstance(other, type(self)):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError

    @classmethod
    def new_product(cls, name, description, color, price, quantity):
        return cls(name, description, color, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = new_price


class Smartphone(Product):
    """Класс для смартфонов (дочерний от Product)"""

    def __init__(self, name: str, description: str, color: str,
                 price: float, quantity: int, efficiency: str, model: str, memory: str):
        """Создание экземпляра класса Smartphone

                    :param efficiency: производительность
                    :param model: модель
                    :param memory: объем встроенной памяти"""

        super().__init__(name, description, color, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        print(super().__repr__)

    @classmethod
    def new_smartphone(cls, name, description, color, price, quantity, efficiency, model, memory):
        return cls(name, description, color, price, quantity, efficiency, model, memory)


class Grass(Product):
    """Класс для газонов (дочерний от Product)"""

    def __init__(self, name: str, description: str, color: str,
                 price: float, quantity: int, maker: str, germination: str):
        """Создание экземпляра класса Smartphone

                    :param maker: страна-производитель
                    :param germination: срок прорастания"""

        super().__init__(name, description, color, price, quantity)
        self.maker = maker
        self.germination = germination

    @classmethod
    def new_grass(cls, name, description, color, price, quantity, maker, germination):
        return cls(name, description, color, price, quantity, maker, germination)
