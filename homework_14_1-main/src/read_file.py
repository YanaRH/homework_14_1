import json

from src.category import Category
from src.product import Product


def read_json_file():
    """Загружает данные категорий и продуктов из JSON файла."""
    with open("data/products.json", "r", encoding="utf8") as file:
        data = json.load(file)

    products = []
    categories = []

    for category_data in data:
        for product_data in category_data["products"]:
            product = Product(
                product_data["name"], product_data["description"], product_data["price"], product_data["quantity"]
            )
            products.append(product)

        category = Category(category_data["name"], category_data["description"], products)
        categories.append(category)

    return categories
