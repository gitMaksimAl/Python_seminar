# -*- coding: utf-8 -*-

# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от -50 до 50

nDays = int(input('Введите количество дней '))
maxDays = 0
days = 0

for i in range(nDays):
    temp = int(input('Значение температуры '))
    if temp >= 0:
       days += 1
    else:
        if maxDays < days:
            maxDays = days
        days = 0

print(maxDays)