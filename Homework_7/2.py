# -*- coding: utf-8 -*-
from typing import Callable

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).


def print_operation_table(func: Callable[[int, int], int], row=6, column=6):
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            print("{0:>3}".format(func(i, j)), end=' ')
        print('')


print_operation_table(lambda x, y: x * y)
