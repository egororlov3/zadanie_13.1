import pytest
from classes import Category
from classes import Product


@pytest.fixture
def goods(products1,products2):
    return Category("sneakers", "new",
                    [products1, products2])


def test_init_category(goods, products2, products1):
    assert goods.name == "sneakers"
    assert goods.description == "new"
    assert goods.products == [products1, products2]
    assert goods.total_categories == 2
    assert goods.total_uniques == 1


@pytest.fixture
def products1():
    return Product("New Balance", "9060 Truffle", 20000, 5)


def test_init_products1(products1):
    assert products1.name == "New Balance"
    assert products1.description == "9060 Truffle"
    assert products1.price == 20000
    assert products1.quantity == 5


@pytest.fixture
def products2():
    return Product("Nike", "Airmax 95 Black", 10000, 10)


def test_init_products2(products2):
    assert products2.name == "Nike"
    assert products2.description == "Airmax 95 Black"
    assert products2.price == 10000
    assert products2.quantity == 10
