# -*- coding: utf-8 -*-

# Найдите сумму цифр трехзначного числа.

num = int(input('Введите трехзначное число: '))

sum = 0
while num > 0:
    sum = sum + (-num % 10 if num < 0 else num % 10)
    num //= 10

print(f'Сумма цифр: {sum}')
