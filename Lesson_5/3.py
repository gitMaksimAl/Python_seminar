# -*- coding: utf-8 -*-

# Напишите функцию, которая принимает одно число и проверяет
# является ли оно простым.

"""
Script take an integer and print out, prime is it or not prime.
"""


def is_prime(num: int) -> bool:
    if num == 2:
        return True
    elif num == 1 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


n = int(input())
print('Prime' if is_prime(n) else 'Not prime')
