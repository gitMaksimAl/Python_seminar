# -*- coding: utf-8 -*-

# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
# максимума)

numbers = [int(i) for i in input('Введите значения массива ').split()]
min_value = int(input('Введите минимальное значение '))
max_value = int(input('Введите максимальное значение '))
indexes = []

for i in range(len(numbers)):
    if min_value <= numbers[i] <= max_value:
        indexes.append(i)

print(*indexes)
