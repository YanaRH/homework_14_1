from src.product import Product
from src.base_category import BaseCategory
from src.exceptions import ZeroQuantityError


class Category(BaseCategory):
    name: str
    description: str
    products: list
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        super().__init__(name, description)
        self.__products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(products) if products else 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}"
        return product_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен.")
            except ZeroQuantityError as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.total_products += 1
                print(f"Товар '{product.name}' добавлен в категорию '{self.name}'.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError

    def avg_price(self):
        try:
            total_price = sum(product.price * product.quantity for product in self.__products)
            avg_price = total_price / sum(product.quantity for product in self.__products)
            return round(avg_price, 1)

        except ZeroDivisionError:
            return 0
