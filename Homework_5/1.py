# -*- coding: utf-8 -*-

# Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии

def power_to(num: int, power: int) -> int:
    if power == 0:
        return 1
    return power_to(num, power - 1) * num


chisloA = int(input('Введите число '))
chisloB = int(input('Введите целую степень '))
print(f"1/{power_to(chisloA, -chisloB)}" if chisloB < 0 else power_to(chisloA, chisloB))
