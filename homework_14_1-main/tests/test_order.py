def test_order_init(order):
    assert order.product.name == "Iphone 15"
    assert order.product.description == "512GB, Gray space"
    assert order.product.price == 210000.0
    assert order.product.quantity == 8
    assert order.description == "512GB, Gray space"
    assert order.name == "Iphone 15"
    assert order.quantity == 5
    assert order.total_price == 1050000.0


def test_order_str(order):
    result = order.__str__()
    assert result == 'Заказ: Iphone 15, Количество: 5, Итоговая стоимость: 1050000.0 руб.'
