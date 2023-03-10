# -*- coding: utf-8 -*-

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

string = input()

dic = {}.fromkeys(string, 0)
print(string)

for i in string:
    print( f"{i}_{dic[i]}" if dic[i] else i, end=' ')
    dic[i] += 1
