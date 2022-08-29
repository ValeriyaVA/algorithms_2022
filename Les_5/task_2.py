"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

"""
достаточно красиво получилось положить числа в словарь
и некрасиво потом длиннющей строкой складывать/умножать ключи словарей
"""

from collections import defaultdict


def num_dict(num):
    number = defaultdict(list)
    for i in num:
        number[int(num, 16)].append(i)
    return number


def calc(num1, num2):
    print(list(hex(list(num_dict(num1).keys())[0] + list(num_dict(num2).keys())[0])[2::]))
    print(list(hex(list(num_dict(num1).keys())[0] * list(num_dict(num2).keys())[0])[2::]))


number_1, number_2 = [i for i in input('Введите через пробел два 16-ных числа: ').split()]
calc(number_1, number_2)
