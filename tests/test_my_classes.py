from unittest.mock import Mock, patch

import pytest

from src.my_classes import Product, Category
from src.utils import data_load_from_json


# тесты для класса Product
def test_product_class_init(product_fixture):
    assert product_fixture.name == "Test_name"
    assert product_fixture.description == "Test description"
    assert product_fixture.price == 54.99
    assert product_fixture.quantity == 65


def test_product_class_price(capsys, product_fixture):
    product_fixture.price = 100  # повышение цены
    assert product_fixture.price == 100

    product_fixture.price = -100  # цена ниже 0
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip()
        == "Product(Test_name, Test description, 54.99, 65)\nЦена не должна быть нулевая или отрицательная"
    )


def test_product_class_price_low_yes(product_fixture):
    with patch("builtins.input", return_value="y") as mock_input:
        product_fixture.price = 34  # понижение цены
        assert product_fixture.price == 34


def test_product_class_price_low_no(product_fixture):
    with patch("builtins.input", return_value="test") as mock_input:
        product_fixture.price = 34  # понижение цены
        assert product_fixture.price == 54.99


def test_new_product_new(user_product_dict):
    test_new_product = Product.new_product(user_product_dict)
    assert test_new_product.name == "Samsa"
    assert test_new_product.description == "Very tasty samsa"
    assert test_new_product.price == 180
    assert test_new_product.quantity == 5


def test_new_product_existing(user_product_dict2):
    test_product2 = Product.new_product(user_product_dict2)
    print(test_product2.product_list)
    assert test_product2.name == "Samsa"
    assert test_product2.description == "Very tasty samsa"
    assert test_product2.price == 180
    assert test_product2.quantity == 100


def test_new_product_from_file():
    assert data_load_from_json("products.json")[0].name == "Смартфоны"


def test_product_class_str(capsys, product_fixture):
    print(product_fixture)
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip()
        == "Product(Test_name, Test description, 54.99, 65)\nTest_name, 54.99 руб. Остаток: 65 шт."
    )


def test_product_class_add(product_fixture, product_2_fixture):
    assert product_fixture + product_2_fixture == 6874.35


# тесты для класса Category
def test_category_class(capsys, category_1_fixture, category_2_fixture):
    assert category_1_fixture.name == "Cat_Test_name"
    assert category_1_fixture.description == "Category Test description"

    category_1_fixture.products
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip().split("\n")[-1]
        == "Test_name3, 354.99 руб. Остаток: 25 шт."
    )

    assert category_2_fixture.name == "Cat_Test_name 2"
    assert category_2_fixture.description == "Category Test description 2"

    assert category_1_fixture.category_count == 4
    assert category_2_fixture.category_count == 4

    assert category_1_fixture.product_count == 149
    assert category_2_fixture.product_count == 149


def test_category_add_product(category_1_fixture):
    category_count_initial = category_1_fixture.product_count
    new_prod = Product("New_name", "New Test description", 4.99, 18)
    category_1_fixture.add_product(new_prod)
    assert category_1_fixture.product_count == category_count_initial + 1


def test_category_class_str(capsys, category_1_fixture):
    print(category_1_fixture)
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip().split("\n")[-1]
        == "Cat_Test_name, количество продуктов: 105 шт."
    )


# тесты для других классов
def test_smartphone_class_init(smartphone1_fixture):
    assert smartphone1_fixture.name == "Xiaomi"
    assert smartphone1_fixture.description == "description norm tel"
    assert smartphone1_fixture.price == 100
    assert smartphone1_fixture.quantity == 5
    assert smartphone1_fixture.efficiency == "efficiency-Xiaomi"
    assert smartphone1_fixture.model == "note 9"
    assert smartphone1_fixture.memory == "128GB"
    assert smartphone1_fixture.color == "White"


def test_lawngrass_class_init(lawngrass1_fixture):
    assert lawngrass1_fixture.name == "Газонная трава"
    assert lawngrass1_fixture.description == "Элитная трава для газона"
    assert lawngrass1_fixture.price == 500
    assert lawngrass1_fixture.quantity == 20
    assert lawngrass1_fixture.country == "Россия"
    assert lawngrass1_fixture.germination_period == "7 дней"
    assert lawngrass1_fixture.color == "Зеленый"


def test_smartphone_class_add(smartphone1_fixture, smartphone2_fixture):
    assert smartphone1_fixture + smartphone2_fixture == 2900


def test_lawngrass_class_add(lawngrass1_fixture, lawngrass2_fixture):
    assert lawngrass1_fixture + lawngrass2_fixture == 16750


def test_different_categories_add(smartphone1_fixture, lawngrass1_fixture):
    with pytest.raises(TypeError):
        result = lawngrass1_fixture + smartphone1_fixture


def test_category_add_product_smartphone(
    capsys, category_1_fixture, smartphone1_fixture
):
    new_prod_smartphone = smartphone1_fixture
    category_1_fixture.add_product(new_prod_smartphone)
    category_1_fixture.products
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip().split("\n")[-1] == "Xiaomi, 100 руб. Остаток: 5 шт."
    )


def test_category_add_product_error(category_1_fixture):
    new_prod_not_product = 1000
    with pytest.raises(
        TypeError,
        match="Нельзя добавить продукт не относящийся к классу Product или его наследникам",
    ):
        category_1_fixture.add_product(new_prod_not_product)


def test_product_class_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        new_product_zero_quantity = Product("Test Testo", "Test Testo's description", 180, 0)


def test_category_middle_price(category_1_fixture):
    assert category_1_fixture.middle_price() == 221.65666666666667


def test_category_middle_price_zero():
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
