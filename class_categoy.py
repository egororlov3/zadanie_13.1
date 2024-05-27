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

    def __str__(self):
        """Выводит новое строковое отображение"""
        return f"Название категории: {self.name}, Количество продутков: {self.__len__()} шт."

    def __len__(self):
        """Подсчитывает количество всез продуктов в одной категории"""
        return sum(product.quantity for product in self.__products)

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

