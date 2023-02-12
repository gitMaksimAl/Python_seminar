# -*- coding: utf-8 -*-

# Требуется найти число Фибоначи, используя рекурсию.


def fibR(num):
    if num < 2:
        return 1
    else:
        return fibR(num - 1) + fibR(num - 2)

n = int(input('Введите число '))
print(fibR(n))
