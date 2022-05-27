'''
Разработать целочисленный генератор случайных чисел. В функцию передавать начальную и конечную границу 
диапазона генерации (выдавать значения из диапазона включая концы). Заполнить этими данными словарь. 
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”, а значене сгенеренное случайное число. 
Вывести содержимое словаря. 
(Усложненный вариант по желанию*): Не использовать стандартный модуль python random.
'''

from pprint import pprint
from random import randint


def int_generator(start: int, end: int):
    while True:
        yield randint(start, end)

generator = int_generator(15, 54)

result = {}
for index in range(10):
    result[f'elem_{index}'] = next(generator)

pprint(result)
