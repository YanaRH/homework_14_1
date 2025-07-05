class ZeroQuantityError(Exception):
    """Исключение для обработки добавления товаров с нулевым количеством"""

    def __init__(self, message=None):
        super().__init__(message)
