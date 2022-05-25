'''
Написать программу «Банковский депозит». 
Клиент банка делает депозит на определенный срок. 

В зависимости от суммы и срока вклада определяется процентная ставка: 
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых). 
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых). 
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых). 

Проценты начисляются на депозит в конце каждого месяца.

Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада 
(в месяцах), а на выходе возвращать сумму вклада на конец срока.

'''

def bank(value: int, period: int):
    percent = None
    if value in range(1000, 10000):
        if period in range(6, 12):
            percent = 0.05
        elif period in range(12, 24):
            percent = 0.06
        elif period >= 24:
            percent = 0.05
    elif value in range(10000, 100000):
        if period in range(6, 12):
            percent = 0.06
        elif period in range(12, 24):
            percent = 0.07
        elif period >= 24:
            percent = 0.065
    elif value in range(100000, 1000000):
        if period in range(6, 12):
            percent = 0.07
        elif period in range(12, 24):
            percent = 0.08
        elif period >= 24:
            percent = 0.075

    for month in range(period):
        value *= 1 + percent / 12
    
    return round(value, 2)


print(bank(100000, 6))
print(bank(1000, 24))
print(bank(10000, 18))
