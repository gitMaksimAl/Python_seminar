# -*- coding: utf-8 -*-

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и
# -1. Также нельзя использовать циклы

def suma_b(a: int, b: int) -> int:
    if b == 0:
        return a
    elif a == 0:
        return b
    return suma_b(a + 1, b - 1)


num_a = int(input())
num_b = int(input())
print(f"Сумма {num_a} + {num_b} = {suma_b(num_a, num_b)}")
