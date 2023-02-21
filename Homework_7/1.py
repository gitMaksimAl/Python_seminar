# -*- coding: utf-8 -*-

# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

vinny_song = input('Спойте песенку винни: ')
vow_ru = "аяеёуюоэиы"


def parsed_song(data: str):
    words = data.lower().split()
    if len(words) <= 1:
        print('Wrong song')
        return None
    else:
        return words


def is_rhythmic(song: list[str] | None, vwls: str):
    check = False
    if song:
        bar = [wd.count(char) for wd in song for char in vwls if char in wd]
        if len(set(bar)) == 1:
            check = True
    return check


if is_rhythmic(parsed_song(vinny_song), vow_ru):
    print('Парам пам-пам')
else:
    print('Пам парам')
