'''
3.	Реализовать возможность переустановки значения цены товара в родительском классе. Проверить, распечатать информацию о товаре.
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
    @staticmethod
    def get_parent_data():
        print(f"{ItemDiscount.get_name()} {ItemDiscount.get_price()}")

    @staticmethod
    def set_parent_price(price):
        ItemDiscount.set_price(price)


parent = ItemDiscount()
child = ItemDiscountReport()

child.set_parent_price(600)
child.get_parent_data()
