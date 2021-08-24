'''2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
'''
import os


def print_directory_contents(sPath):
    dir_lst = os.listdir(sPath)

    for item in dir_lst:

        f_Path = os.path.join(sPath, item)
        if os.path.isfile(f_Path):
            print(item)
        if os.path.isdir(f_Path):
            print_directory_contents(f_Path)

print_directory_contents('C:\\Users\\marin\\GB')