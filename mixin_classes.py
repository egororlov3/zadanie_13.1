class MixinProd:

    def __repr__(self):
        products = [f'{x}, {y}' for x, y in self.__dict__.items()]
        return f'{self.__class__.__name__} {", ".join(products)}'

