from unittest.mock import Mock, patch
from src.my_classes import Product


# тесты для класса Product

def test_product_class_init(product_fixture):
    assert product_fixture.name == "Test_name"
    assert product_fixture.description == "Test description"
    assert product_fixture.price == 54.99
    assert product_fixture.quantity == 65


def test_product_class_price(capsys, product_fixture):
    product_fixture.price = 100 # повышение цены
    assert product_fixture.price == 100

    product_fixture.price = -100 # цена ниже 0
    screen_message = capsys.readouterr()
    assert screen_message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_class_price_low_yes(product_fixture):
    with patch('builtins.input', return_value='y') as mock_input:
        product_fixture.price = 34  # понижение цены
        assert product_fixture.price == 34


def test_product_class_price_low_no(product_fixture):
    with patch('builtins.input', return_value='test') as mock_input:
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
    assert test_product2.name == "Samsa"
    assert test_product2.description == "Very tasty samsa"
    assert test_product2.price == 180
    assert test_product2.quantity == 100


def test_product_class_str(capsys, product_fixture):
    print(product_fixture)
    screen_message = capsys.readouterr()
    assert screen_message.out.strip() == "Test_name, 54.99 руб. Остаток: 65 шт."

def test_product_class_add(product_fixture, product_2_fixture):
    assert product_fixture + product_2_fixture == 6874.35


# тесты для класса Category

def test_category_class(capsys, category_1_fixture, category_2_fixture):
    assert category_1_fixture.name == "Cat_Test_name"
    assert category_1_fixture.description == "Category Test description"

    category_1_fixture.products
    screen_message = capsys.readouterr()
    assert screen_message.out.strip() == 'Test_name, 54.99 руб. Остаток: 65 шт.\n\nTest_name2, 254.99 руб. Остаток: 15 шт.\n\nTest_name3, 354.99 руб. Остаток: 25 шт.'

    assert category_2_fixture.name == "Cat_Test_name 2"
    assert category_2_fixture.description == "Category Test description 2"

    assert category_1_fixture.category_count == 2
    assert category_2_fixture.category_count == 2

    assert category_1_fixture.product_count == 115
    assert category_2_fixture.product_count == 115


def test_category_add_product(category_1_fixture):
    category_count_initial = category_1_fixture.product_count
    new_prod = Product("New_name", "New Test description", 4.99, 18)
    category_1_fixture.add_product(new_prod)
    assert category_1_fixture.product_count == category_count_initial + 1

def test_category_class_str(capsys, category_1_fixture):
    print(category_1_fixture)
    screen_message = capsys.readouterr()
    assert screen_message.out.strip() == "Cat_Test_name, количество продуктов: 105 шт."
