from src.my_classes import Product, Smartphone, LawnGrass


def test_print_mixin_product(capsys):
    my_prod = Product("Test_name", "Test description", 54.99, 65)
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip() == "Product(Test_name, Test description, 54.99, 65)"
    )


def test_print_mixin_smartphone(capsys):
    my_smartphone = Smartphone(
        "Xiaomi",
        "description norm tel",
        100,
        5,
        "efficiency-Xiaomi",
        "note 9",
        "128GB",
        "White",
    )
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip() == "Smartphone(Xiaomi, description norm tel, 100, 5)"
    )


def test_print_mixin_lawngrass(capsys):
    my_lawngrass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    screen_message = capsys.readouterr()
    assert (
        screen_message.out.strip()
        == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
    )
