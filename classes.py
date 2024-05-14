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
        self.products = products
        Category.total_categories += len(set([product.name for product in products]))
        Category.total_uniques += 1


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
        self.price = price
        self.quantity = quantity
