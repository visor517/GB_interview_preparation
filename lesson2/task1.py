'''
1.	Создать два класса. Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: 
название и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data), отвечающую 
за отображение информации о товаре в одной строке вида (“{название товара} {цена товара}”). Создать экземпляры 
родительского класса и дочернего. Распечатать информацию о товаре.
'''

class ItemDiscount():
    name = "Товар"
    price = 5400


class ItemDiscountReport(ItemDiscount):
    @staticmethod
    def get_parent_data():
        print(f"{ItemDiscount.name} {ItemDiscount.price}")


parent = ItemDiscount()
child = ItemDiscountReport()

child.get_parent_data()
