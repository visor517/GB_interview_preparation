'''
2.	Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей логики 
работы программы будет сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким образом, чтобы получить 
доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.
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


class ItemDiscountReport(ItemDiscount):
    @staticmethod
    def get_parent_data():
        print(f"{ItemDiscount.get_name()} {ItemDiscount.get_price()}")


parent = ItemDiscount()
child = ItemDiscountReport()

child.get_parent_data()
