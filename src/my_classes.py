class Product:
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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                users_price_answer = input("Согласны лм вы понизить цену?['y' - да, остальное - нет]")
                if users_price_answer == "y":
                    self.__price = new_price
            else:
                self.__price = new_price


    @classmethod
    def new_product(cls, user_product_dict: dict):
        if Product.product_list:
            for prod in Product.product_list:
                if prod.name == user_product_dict["name"]:
                    prod.quantity +=  user_product_dict["quantity"]
                    prod.__price = max(prod.__price, user_product_dict["price"])
                    return prod
        else:
            new_user_product = Product(**user_product_dict)
            Product.product_list.append(new_user_product)
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

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += new_product.quantity # хотя в дз написано прибавлять 1 к класс-атрибуту «счетчик продуктов». НО это неверно.

    @property
    def products(self):
        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")




# # my cheking:
# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 17)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3])
#
# # print(category1.products)
# product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
# category1.add_product(product4)
# # print(category1.products)
# # print(category1.product_count)
#
# new_product = Product.new_product(
#     {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#      "quantity": 5})
# print(new_product.name)
# print(new_product.description)
# print(new_product.price)
# print(new_product.quantity)
#
# new_product.price = 800
# print(new_product.price)

# new_product.price = -100
# print(new_product.price)
# new_product.price = 0
# print(new_product.price)
