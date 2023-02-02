# -*- coding: utf-8 -*-

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза

N = int(input('Сколько арбузов '))

maxweight = minweight = int(input('Вес арбуза '))

for _ in range(N - 1):
    weight = int(input('Вес арбуза '))
    if weight < minweight:
        minweight = weight
    if weight > maxweight:
        maxweight = weight

print(minweight, maxweight)
