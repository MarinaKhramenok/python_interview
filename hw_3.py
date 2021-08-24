'''3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться
по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.'''
import random


def generator(n1, n2):
    if n1!=0 and n2!=0:
        gen_lst =[]
        gen_dic = {}
        for elem in range(5):
            gen = random.randint(n1, n2)
            gen_lst.append(gen)
            gen_dic.update({'elem_{}'.format(elem+1): gen})
    return (gen_lst, gen_dic)


print(generator(5, 10))
