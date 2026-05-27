from src.mixin_classes import PrintMixin


def test_print_mixin_product(capsys, product_fixture):
    my_prod = product_fixture
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip() == "Product(Test_name, Test description, 54.99, 65)"
    )


def test_print_mixin_smartphone(capsys, smartphone1_fixture):
    my_smartphone = smartphone1_fixture
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip() == "Smartphone(Xiaomi, description norm tel, 100, 5)"
    )


def test_print_mixin_lawngrass(capsys, lawngrass1_fixture):
    my_lawngrass = lawngrass1_fixture
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip()
        == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
    )
