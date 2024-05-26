import pytest
from classes import Category
from classes import Product


@pytest.fixture
def goods(product1, product2):
    return Category("sneakers", "new",
                    [product1, product2])


def test_init_category(goods, product2, product1):
    assert goods.name == "sneakers"
    assert goods.description == "new"
    assert goods.products == [product1, product2]
    assert goods.total_categories == 2
    assert goods.total_uniques == 1


@pytest.fixture
def product1():
    return Product("New Balance", "9060 Truffle", 20000, 5)


def test_init_products1(product1):
    assert product1.name == "New Balance"
    assert product1.description == "9060 Truffle"
    assert product1.price == 20000
    assert product1.quantity == 5


@pytest.fixture
def product2():
    return Product("Nike", "Airmax 95 Black", 10000, 10)


def test_init_products2(product2):
    assert product2.name == "Nike"
    assert product2.description == "Airmax 95 Black"
    assert product2.price == 10000
    assert product2.quantity == 10




