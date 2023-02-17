# -*- coding: utf-8 -*-

# Составьте программу для решения задачи. Два натуральных числа называются
# дружественными, если каждое из них равно сумме всех делителей другого (само
# другое число в качестве делителя не рассматривается). Например, 220
# (1+2+4+5+10+11+20+22+44+55+110=284) и 284 (1+2+4+71+142=220) – дружественные
# числа. Пары необходимо выводить по одной в строке, разделяя пробелами. Найти
# все пары натуральных дружественных чисел, меньших 10 000


def pair(value):
    sq_num = int(value ** 0.5)
    res = 1 + (0 if sq_num ** 2 != value else sq_num)

    for i in range(2, sq_num):
        if value % i == 0:
            res += i + value // i
    return res


for j in range(10, 300):
    sum1 = pair(j)
    sum2 = pair(sum1)

    # Если второе число равно j и первое число меньше второго
    # Второе условие защита от дубликатов,
    # записанных наоборот
    if sum2 == j and sum1 < sum2:
        print(j, sum1)