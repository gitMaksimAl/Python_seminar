# -*- coding: utf-8 -*-

# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

chisloA = int(input())
fib1 = 0
fib2 = 1
i = 2

while fib2 <= chisloA:
    if fib2 == chisloA:
        print(i)
        break
    fib1, fib2 = fib2, fib1 + fib2
    i += 1
else:
    print(-1)
