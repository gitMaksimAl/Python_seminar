# -*- coding: utf-8 -*-

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих строках записаны N целых чисел
# Ai. Последняя строка содержит число X

amount = int(input('Количество элементов '))

listA = []
for i in range(amount):
    listA.append(int(input('Введите число ')))
numX = int(input('Введите число Х '))
if numX not in listA:
    listA.append(numX)
listA.sort()
too_close = listA.index(numX)

print(*listA)
print(listA[too_close - 1] if too_close != 0 else listA[too_close])
