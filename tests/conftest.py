import pytest
from src.my_classes import Product, Category


@pytest.fixture
def product_fixture():
    return Product("Test_name", "Test description", 54.99, 65)


@pytest.fixture
def category_fixture():
    return Category("Cat_Test_name", "Category Test description", [
        Product("Test_name", "Test description", 54.99, 65),
        Product("Test_name2", "Test description2", 254.99, 265),
        Product("Test_name3", "Test description3", 354.99, 365)
    ])


