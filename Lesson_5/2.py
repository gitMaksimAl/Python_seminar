# -*- coding: utf-8 -*-

# Хакер Вася получил доступ к классному журналу и хочет
# заменить все свои минимальные оценки на максимальные.
# Напишите программу которая заменяет оценки но наоборот
# макимальные на минимальные.

def max_to_min(lst):
    min_grade = min(lst)
    max_grade = max(lst)
    return [min_grade if i == max_grade else i for i in lst]


n = int(input('Сколько оценок? '))
lst = [int(input()) for i in range(n)]
print(*max_to_min(lst))
