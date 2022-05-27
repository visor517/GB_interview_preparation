'''
Вывести таблицу умножения в виде. 
'''

n = int(input("Введите N: "))

for x in range(1, n + 1):
    for y in range(1, 11):
        print(f'{x} x {y} = {x*y}')

    print('-'*5)