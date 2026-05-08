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
