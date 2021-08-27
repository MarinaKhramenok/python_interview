'''6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в
первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение
каждой из функции тремя способами.'''
class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReportFirst(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReportSecond(ItemDiscount):
    def get_info(self):
        print(self.price)


first = ItemDiscountReportFirst('apple', 15)
first.get_info()

second = ItemDiscountReportSecond('peach', 30)
second.get_info()

for obj in (first, second):
    obj.get_info()


def obj_handler(obj):
    obj.get_info()


obj_handler(first)
obj_handler(second)