'''
Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, 
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они 
совпадают, программа должна возвращать значение True, иначе False.
'''

def check_number():
    number = input('Введите число: ')

    if ',' in number:
        print('Число дробное')
        integer_part, fractional_part = number.split(',')
        if integer_part == fractional_part:
            return True
        else:
            return False
    else:
        print('Число целое')    


print(check_number())
