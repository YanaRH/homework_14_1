import pytest


def test_lawn_grass_init(lawn_grass1):
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.description == "Элитная трава для газона"
    assert lawn_grass1.price == 500.0
    assert lawn_grass1.quantity == 20
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_lawn_grass_add(lawn_grass1, lawn_grass2):
    assert lawn_grass1 + lawn_grass2 == 16750


def test_lawn_grass_add_error(lawn_grass1):
    with pytest.raises(TypeError):
        result = lawn_grass1 + 1
