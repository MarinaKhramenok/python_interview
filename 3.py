'''
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
 Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
 в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
'''
import string

keys = list(string.ascii_lowercase)
values = list(range(10))

def key_val(keys, values):
    values.extend([None] * (len(keys) - len(values)))
    print({key: value for key, value in zip(keys, values)})

key_val(keys, values)
