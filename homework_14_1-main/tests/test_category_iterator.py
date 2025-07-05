import pytest


def test_category_iterator(category_iterator):
    assert category_iterator.index == 0
    assert str(next(category_iterator)) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(next(category_iterator)) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."

    with pytest.raises(StopIteration):
        next(category_iterator)
