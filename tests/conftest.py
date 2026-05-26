import pytest
from src.my_classes import Product, Category, Smartphone, LawnGrass


@pytest.fixture
def product_fixture():
    return Product("Test_name", "Test description", 54.99, 65)


@pytest.fixture
def product_2_fixture():
    return Product("Testo", "Testo's description", 100, 33)


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
    return {
        "name": "Samsa",
        "description": "Very tasty samsa",
        "price": 180,
        "quantity": 5,
    }


@pytest.fixture
def user_product_dict2():
    return {
        "name": "Samsa",
        "description": "Very tasty samsa",
        "price": 135,
        "quantity": 95,
    }


@pytest.fixture
def smartphone1_fixture():
    return Smartphone(
        "Xiaomi",
        "description norm tel",
        100,
        5,
        "efficiency-Xiaomi",
        "note 9",
        "128GB",
        "White",
    )


@pytest.fixture
def smartphone2_fixture():
    return Smartphone(
        "Sony",
        "description norm Sonyl",
        200,
        12,
        "efficiency-Sony",
        "Super model",
        "64GB",
        "Grey",
    )


@pytest.fixture
def lawngrass1_fixture():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def lawngrass2_fixture():
    return LawnGrass(
        "Газонная super трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
