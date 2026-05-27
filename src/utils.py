import json
from config import PATH_data
from src.my_classes import Category, Product


def data_load_from_json(path_json):
    """Функция считывает данные мз JSON-файла и подгружает данные
    по категориям и товарам, чтобы конвертировать их в объекты"""

    path_to_file = str(PATH_data) + "\\" + path_json
    categories = []

    with open(path_to_file, "r", encoding="UTF-8") as file:
        data = json.load(file)

    for user_category in data:
        products = []
        for product in user_category["products"]:
            products.append(Product(**product))
        user_category["products"] = products
        categories.append(Category(**user_category))

    return categories
