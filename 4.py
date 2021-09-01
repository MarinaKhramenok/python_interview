'''
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
'''
import os
import random
import string


def create_txt_file(f_name):
    def print_file(f_name):
        with open(f_name, 'r', encoding='utf-8') as f:
            for line in f:
                print(line)

    if os.path.isfile(f_name) :
        print('файл с таким именем уже существует')
    else:
        with open(f_name, 'w', encoding='utf-8') as f:
            keys = [(''.join(random.choice(string.ascii_lowercase) for _ in range(10))) for _ in range(10)]
            values = [random.randint(1, 100) for _ in range(10)]
            f.writelines(['{}{} \n'.format(key, value) for key, value in zip(keys, values)])
    return print_file(f_name)

create_txt_file('hw.txt')