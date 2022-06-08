'''
5.	Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса. 
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать 
за вывод названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
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


class ItemDiscountReport1(ItemDiscount):
    def get_info(self):
        print(ItemDiscount.get_name())


class ItemDiscountReport2(ItemDiscount):
    def get_info(self):
        print(ItemDiscount.get_price())


ItemDiscountReport1().get_info()
ItemDiscountReport2().get_info()
