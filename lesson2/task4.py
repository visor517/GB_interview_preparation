'''
4.	Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс. 
Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна передаваться переменная — 
скидка), и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — 
цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая и 
третья строка после объявления дочернего класса).
'''

class ItemDiscount():
    __name = "Товар"
    __price = 5400

    @classmethod
    def get_name(cls):
        return cls.__name

    @classmethod
    def get_price(cls):
        return cls.__price

    @classmethod
    def set_price(cls, price):
        cls.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, discount):
        self.discount = discount

    def __str__(self):
        return str(ItemDiscount.get_price() * (1 - self.discount / 100))

    @staticmethod
    def get_parent_data():
        print(f"{ItemDiscount.get_name()} {ItemDiscount.get_price()}")

    @staticmethod
    def set_parent_price(price):
        ItemDiscount.set_price(price)


parent = ItemDiscount()
child = ItemDiscountReport(10)

print(child)