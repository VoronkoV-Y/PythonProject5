class Product():
    """класс Product для создания продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category():
    """класс Category для создания категорий"""
    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += sum([x.quantity for x in self.products])
        # Category.product_count += len(self.products) в случае, если нужно считать общее количество разновидностей товаров


# Моя проверка
if __name__ == "__main__":
    print(Category("Waters", "Some different waters", [Product("1", "11", 130, 4), Product("2", "211", 2130, 24)]).products_quantity)