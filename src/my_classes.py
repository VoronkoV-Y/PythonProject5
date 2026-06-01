from src.base_classes import BaseProduct
from src.mixin_classes import PrintMixin


class Product(PrintMixin, BaseProduct):
    """класс Product для создания продуктов"""

    product_list = []

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.product_list.append(self)
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) == self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                users_price_answer = input(
                    "Согласны лм вы понизить цену?['y' - да, остальное - нет]"
                )
                if users_price_answer == "y":
                    self.__price = new_price
            else:
                self.__price = new_price

    @classmethod
    def new_product(cls, user_product_dict: dict):
        if Product.product_list:
            for prod in Product.product_list:
                if prod.name == user_product_dict["name"]:
                    prod.quantity += user_product_dict["quantity"]
                    prod.__price = max(prod.__price, user_product_dict["price"])
                    return prod
            else:
                new_user_product = Product(**user_product_dict)
                return new_user_product
        else:
            new_user_product = Product(**user_product_dict)
            return new_user_product


class Category:
    """класс Category для создания категорий"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += sum([x.quantity for x in self.__products])

    def __str__(self):
        quantity = sum(
            [x.quantity for x in self.__products]
        )  # согласно ДЗ зачем-то повторяем код из инициализации
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError(
                "Нельзя добавить продукт не относящийся к классу Product или его наследникам"
            )

    @property
    def products(self):
        for product in self.__products:
            # print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
            print(product)
            print()

        return self.__products


class Smartphone(Product):
    """Класс категории Смартфонов"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс категории Травы газонной"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
