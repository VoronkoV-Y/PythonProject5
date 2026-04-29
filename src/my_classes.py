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
    categorys_quantity = 0
    products_quantity = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.categorys_quantity += 1
        Category.products_quantity = len(self.products)


# Моя проверка
if __name__ == "__main__":
    print(Category("Waters", "Some different waters", [Product("1", "11", 130, 4), Product("2", "211", 2130, 24)]))