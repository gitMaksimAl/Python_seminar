# -*- coding: utf-8 -*-

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова. Будем считать, что на вход подается только одно слово, которое содержит
# либо только английские, либо только русские буквы

eng_ru = {
    1: 'AEIOULNSTRАВЕИНОРСТ',
    2: 'DGДКЛМПУ',
    3: 'BCMPБГЁЬЯ',
    4: 'FHVWYЙЫ',
    5: 'KЖЗХЦЧ',
    8: 'JXШЭЮ',
    10: 'QZФЩЪ'
}

word = input('Введите слово ').upper()
# Unfortunately, 1000 lines of C-code do not fit into one line of PEP 8.
# Need more encapsulation here
price = [i for i in eng_ru.keys() for j in range(len(word)) if word[j] in eng_ru[i]]

print(sum(i for i in price))
