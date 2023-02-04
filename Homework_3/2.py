# -*- coding: utf-8 -*-

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих строках записаны N целых чисел
# Ai. Последняя строка содержит число X

amount = int(input('Количество элементов '))

too_close = 0
listA = []
for i in range(amount):
    listA.append(int(input('Введите число ')))
numX = int(input('Введите число Х '))

diff = listA[0] - numX if numX < listA[0] else numX - listA[0]
for i in range(1, amount):
    diff2 = listA[i] - numX if numX < listA[i] else numX - listA[i]
    if diff > diff2:
        diff = diff2
        too_close = i

print(listA[too_close])
