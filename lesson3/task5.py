'''
Расширить программу из п. 4:
а. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений 
(выбирается случайно) заменить на значения типа 345example (в обратном порядке, число и строка). (То есть вы 
переделываете функцию записи в файл так, чтобы она иногда меняла запись на 345example)
б. Реализовать функцию поиска определенных подстрок в файле по следующим условиям: вывод первого вхождения, 
вывод всех вхождений.
в. Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
(это ДВЕ ОТДЕЛЬНЫЕ функции которые ВЫВОДЯТ значения, не записывают и не модифицируют файлы)
'''

import os
from random import randint


def create_file(name):
    file_name = f'{name}.txt'
    if not os.path.exists(file_name):
        list_txt = (item for item in ['test', 'rest', 'quest', 'guest', 'Cuba'])
        list_num = (item for item in [125, 137, 457, 145, 909])

        with open(file_name, 'w') as file:
            for item in zip(list_txt, list_num):
                if randint(0,1):
                    file.writelines(f'{item[0]}{item[1]}\n')
                else:
                    file.writelines(f'{item[1]}{item[0]}\n')

        print_file(file_name)
        find_line(file_name, 'st1')
        change_line(file_name, 'st1', 'plug')
    else:
        print(f'Файл {name} уже существует')


def print_file(file_name):
    with open(file_name, 'r') as file:
        print(file.read())


def find_line(file_name: str, text: str, all=False):
    with open(file_name, 'r') as file:
        file_text = file.read()

        for line in file_text.split('\n'):
            index = line.find(text)
            if index >= 0:
                print(line)
            if not all:
                break

def change_line(file_name: str, text: str, plug: str):
    with open(file_name, 'r') as file:
        file_text = file.read()

        for line in file_text.split('\n'):
            index = line.find(text)
            if index >= 0:
                print(f'{line[:index]}{plug}{line[index+len(text):]}')


create_file('test')
