# -*- coding: utf-8 -*-

# Дано натуральное число. Требуется определить, является ли
# год с данным номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO. Напомним, что в соответствии
# с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

year = int(input('Напишите год, чтобы узнать високосный он или нет... '))

if (year % 4 == 0 and year % 100) or year % 400 == 0:
    print(f'{year} - високосный.')
else:
    print(f'{year} - не високосный.')