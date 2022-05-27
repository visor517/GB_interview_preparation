'''
Реализовать функцию print_directory_contents(path). Функция принимает имя директории и выводит ее содержимое, включая содержимое всех
поддиректории (рекурсивно вызывая саму себя). Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile
'''

import os


def print_directory_contents(path):
    for item in os.listdir(path):
        print(item)

        new_path = f'{path}/{item}'

        if not os.path.isfile(new_path):
            print_directory_contents(new_path)


print_directory_contents('d:/GB/preparation')
