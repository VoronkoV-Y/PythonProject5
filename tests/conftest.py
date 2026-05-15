import pytest
from src.my_classes import Product, Category


@pytest.fixture
def product_fixture():
    return Product("Test_name", "Test description", 54.99, 65)


@pytest.fixture
def category_1_fixture():
    return Category(
        "Cat_Test_name",
        "Category Test description",
        [
            Product("Test_name", "Test description", 54.99, 65),
            Product("Test_name2", "Test description2", 254.99, 15),
            Product("Test_name3", "Test description3", 354.99, 25),
        ],
    )


@pytest.fixture
def category_2_fixture():
    return Category(
        "Cat_Test_name 2",
        "Category Test description 2",
        [Product("Test_name 2", "Test description 2", 154.99, 10)],
    )


@pytest.fixture
def user_product_dict():
    return {"name": "Samsa", "description": "Very tasty samsa", "price": 180,
         "quantity": 5}


@pytest.fixture
def user_product_dict2():
    return {"name": "Samsa", "description": "Very tasty samsa", "price": 135,
         "quantity": 95}