'''
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения. 
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в 
словаре для него должно сохраняться значение None. Если есть  значения, которым не хватило ключей, их необходимо 
отбросить.
'''

def create_dict(keys: list, values: list):
    if len(keys) > len(values):
        for _ in range(len(keys) - len(values)):
            values.append(None)
            
    return {key: values[i] for i, key in enumerate(keys)}


print(create_dict(['A', 'B', 'C', 'D'], [1, 2, 3, 4, 5]))
print(create_dict(['A', 'B', 'C', 'D', 'E'], [1, 2, 3, 4, 5]))
print(create_dict(['A', 'B', 'C', 'D', 'E'], [1, 2, 3, 4]))
