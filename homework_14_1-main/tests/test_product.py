from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product


def test_product_initialization():
    product = Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )

    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_count():
    prod_list = []
    category = Category(
        name="Смартфоны", description="Смартфоны, как средство не только коммуникации", products=prod_list
    )
    assert Category.total_products == 0


def test_new_product_creation():
    products = []
    product_data = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}

    new_product = Product.new_product(product_data, products)

    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.price == 210000.0
    assert new_product.quantity == 8
    assert len(products) == 1
    assert products[0] == new_product


def test_existing_product_update():
    product1 = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    products = [product1]

    product_data = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 220000.0,  # более высокая цена
        "quantity": 5,  # добавление к количеству
    }

    updated_product = Product.new_product(product_data, products)

    assert updated_product == product1
    assert updated_product.price == 220000.0  # проверка обновления цены на более высокую
    assert updated_product.quantity == 13  # проверка обновления количества


@patch("builtins.input", return_value="y")
def test_price_decrease_confirmation_yes(mock_input):
    product = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)

    product.price = 190000.0  # пытаемся понизить цену

    assert product.price == 190000.0  # цена изменилась, т.к. ввели "y"


@patch("builtins.input", return_value="n")
def test_price_decrease_confirmation_no(mock_input):
    product = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)

    product.price = 190000.0  # пытаемся понизить цену

    assert product.price == 210000.0  # цена не изменилась, т.к. ввели "n"


def test_prevent_negative_or_zero_price():
    product = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)

    product.price = -5000.0  # пытаемся установить отрицательную цену
    assert product.price == 210000.0  # цена не изменилась

    product.price = 0.0  # пытаемся установить нулевую цену
    assert product.price == 210000.0  # цена не изменилась


def test_product_str():
    # Проверка строкового представления продукта
    product = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    expected_output = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product) == expected_output


def test_product_add():
    product1 = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    product2 = Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )

    total_price = product1 + product2
    expected_total = 210000.0 * 8 + 180000.0 * 5  # Общая стоимость всех продуктов
    assert total_price == expected_total


if __name__ == "__main__":
    pytest.main()
