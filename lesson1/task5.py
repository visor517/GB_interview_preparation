'''
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная 
ежемесячная сумма пополнения вклада. Считаем, что клиент вносит средства в последний день каждого месяца, кроме 
первого и последнего. Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.

'''

def bank(value: int, period: int, refil: int):
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
        if month > 0 and month < period - 1:
            value += refil
    
    return round(value, 2)


print(bank(1000, 12, 5000))

