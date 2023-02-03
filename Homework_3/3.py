# -*- coding: utf-8 -*-

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова. Будем считать, что на вход подается только одно слово, которое содержит
# либо только английские, либо только русские буквы

eng_dict = {
    1: 'AEIOULNSTR',
    2: 'DG',
    3: 'BCMP',
    4: 'FHVWY',
    5: 'K',
    8: 'JX',
    10: 'QZ'
}

ru_dict = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЁЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ШЭЮ',
    10: 'ФЩЪ',
}

word = input('Введите слово ').upper()
# Unfortunately, 1000 lines of C-code do not fit into one line of PEP 8.
# Need more encapsulation here
price = [i for i in eng_dict.keys() for j in range(len(word)) if word[j] in eng_dict[i]]

print(word)
print(sum(i for i in price))
