import pytest

from src.category_iterator import CategoryIterator
from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.order import Order
from src.smartphone import Smartphone


@pytest.fixture
def product1():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product2():
    return Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def category1():
    return Category(
        name="Смартфоны",
        description="Смартфоны для всех",
        products=[
            Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
            Product(
                name="Samsung Galaxy C23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
            ),
        ],
    )


@pytest.fixture
def category_iterator(category1):
    iterator = CategoryIterator(category1)
    return iterator


@pytest.fixture
def smartphone1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone2():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def lawn_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


product_for_order = Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def order():
    order = Order(product_for_order, 5)
    return order


@pytest.fixture
def category_without_product():
    return Category(
        name="Смартфоны",
        description="Смартфоны для всех",
        products=[])
