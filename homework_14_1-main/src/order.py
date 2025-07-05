from src.base_category import BaseCategory
from src.product import Product
from src.exceptions import ZeroQuantityError


class Order(BaseCategory):
    def __init__(self, product: Product, quantity: int):
        try:
            if product.quantity == 0:
                raise ZeroQuantityError("Нельзя заказать товар с нулевым количеством.")
        except ZeroQuantityError as e:
            print(str(e))
        else:
            super().__init__(product.name, product.description)
            self.product = product
            self.quantity = quantity
            self.total_price = self.calculate_total_price()
            print("Заказ успешно создан")
        finally:
            print("Обработка создания заказа завершена")

    def calculate_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (f"Заказ: {self.product.name}, Количество: {self.quantity}, "
                f"Итоговая стоимость: {self.total_price} руб.")
