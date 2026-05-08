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
