def test_product_class(product_fixture):
    assert product_fixture.name == "Test_name"
    assert product_fixture.description == "Test description"
    assert product_fixture.price == 54.99
    assert product_fixture.quantity == 65


def test_category_class(category_1_fixture, category_2_fixture):
    assert category_1_fixture.name == "Cat_Test_name"
    assert category_1_fixture.description == "Category Test description"
    assert len(category_1_fixture.products) == 3

    assert category_2_fixture.name == "Cat_Test_name 2"
    assert category_2_fixture.description == "Category Test description 2"
    assert len(category_2_fixture.products) == 1

    assert category_1_fixture.category_count == 2
    assert category_2_fixture.category_count == 2

    assert category_1_fixture.product_count == 115
    assert category_2_fixture.product_count == 115
