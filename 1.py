'''
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение»
из этого пути имени файла (без расширения).
'''
import os


def file_name(f_name):
    f_path = os.path.abspath(f_name)
    return f_path.split('\\')[-1].split('.')[0]

print(file_name('1.py'))

