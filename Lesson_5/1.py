# -*- coding: utf-8 -*-

# Требуется найти число Фибоначи, используя рекурсию.


def fibo(num):
    if num < 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


n = int(input('Введите число '))
print(fibo(n))
