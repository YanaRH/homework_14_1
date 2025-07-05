import pytest

from src.category import Category
from src.product import Product


def test_category_initialization():
    # Проверка корректности инициализации объекта Category
    category = Category(name="Смартфоны", description="Смартфоны для всех")
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны для всех"
    assert Category.total_categories == 1


def test_category_count():
    Category.total_categories = 0
    category1 = Category(name="Смартфоны", description="Смартфоны, как средство не только коммуникации")
    category2 = Category(name="Телевизоры", description="Современные телевизоры для удобного просмотра")

    assert Category.total_categories == 2


def test_add_product():
    # Проверка добавления продукта в категорию
    category = Category(name="Смартфоны", description="Смартфоны для всех")
    product = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    category.add_product(product)

    assert category.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_category_str():
    category_empty = Category(name="Смартфоны", description="Смартфоны для всех")
    assert str(category_empty) == "Смартфоны, количество продуктов: 0 шт."

    product1 = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    product2 = Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )

    category_with_products = Category(
        name="Смартфоны", description="Смартфоны для всех", products=[product1, product2]
    )
    assert str(category_with_products) == "Смартфоны, количество продуктов: 13 шт."


def test_add_product_error():
    category = Category(name="Смартфоны", description="Смартфоны для всех")
    with pytest.raises(TypeError):
        category.add_product(1)


def test_avg_price(category1, category_without_product):
    assert category1.avg_price() == 198461.5
    assert category_without_product.avg_price() == 0


def test_custom_exception(capsys, category1):
    assert len(category1.products_list) == 2

    prod_add = Product(name="Iphone 14", description="512GB, Gray space", price=200000.0, quantity=0)
    category1.add_product(prod_add)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == "Товар с нулевым количеством не может быть добавлен."
    assert message.out.strip().split('\n')[-1] == "Обработка добавления товара завершена."


if __name__ == "__main__":
    pytest.main()
