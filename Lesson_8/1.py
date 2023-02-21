# -*- coding: utf-8 -*-

from os import path

# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

file_db = 'phone_book.txt'
records = []
member_skel = {'id': '',
               'f_name': '',
               'l_name': '',
               'sur_name': '',
               'phone': ''}

if not path.exists(file_db):
    with open(file_db, 'w', encoding='utf-8') as _:
        pass


def show_menu():
    print("1) Показать книгу.\t2) Найти человека.\n3) Добавить человека.\t4) Удалить человека.")
    print("Для выхода введите 'q'.")


def read_db():
    global file_db
    global records

    pass


def save_db():
    global file_db
    global records

    pass


def find_one():
    member = input('Введите имя, фамилию, или id человека из книги')
    pass


def add_one():
    global member_skel

    for key in member_skel.keys():
        member_skel[key] = input(f"{key}")
    pass


def del_one():
    memb = input('Введите имя, фамилию, или id человека из книги')
    pass


def main():
    choice = ''
    while choice != 'q':
        match choice:
            case '1':
                find_one()
                show_menu()
                choice = input()
            case '2':
                add_one()
                show_menu()
                choice = input()
            case '3':
                del_one()
                show_menu()
                choice = input()
            case _:
                print('Wrong input.')
                show_menu()
                choice = input()

main()