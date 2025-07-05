import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Iphone 15"
    assert smartphone1.description == "512GB, Gray space"
    assert smartphone1.price == 210000.0
    assert smartphone1.quantity == 8
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "15"
    assert smartphone1.memory == 512
    assert smartphone1.color == "Gray space"


def test_smartphones_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000.0


def test_smartphones_add_error(smartphone1):
    with pytest.raises(TypeError):
        result = smartphone1 + 1
