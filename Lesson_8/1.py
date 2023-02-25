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


def show_menu():
    print("1) Показать книгу.\t2) Найти человека.\n3) Добавить человека.\t4) Удалить человека.")
    print("Для выхода введите 'q'.")


def read_db():
    global file_db
    global records

    with open(file_db, 'r') as f:
        for line in f.readlines():
            records.append(line.rstrip('\n'))


def save_db():
    global file_db
    global records

    with open(file_db, 'w', encoding='utf-8') as f:
        for i in records:
            f.write(i + '\n')
    print('Phonebook saved.')


def find_one():
    global records

    member = input('Введите имя, фамилию, или id человека из книги ')
    for record in records:
        for i in record.split():
            if member == i:
                print(record)


def add_one():
    global record_template
    global records
    global i_d

    for key in member_skel.keys():
        member_skel[key] = input(f"{key} ")
    record = ' '.join(member_skel.values())
    for one in records:
        if record == one[2:]:
            print('Невозможно добавить запись. Данная запись уже существует.')
            return False
    records.append(f"{i_d} {record}")
    i_d += 1
    return True


def correct_ids():
    global records
    count = 0

    for i in range(len(records)):
        records[i] = str(count) + ' ' + ' '.join(records[i].split()[1:])
        count += 1


def del_one():
    memb = input('Введите имя, фамилию, или id человека из книги')
    for record in records:
        for i in record.split():
            if memb == i:
                print(f"Чтобы удалить эту запись нажмите 'Enter'\n{record}")
                if input() == '':
                    records.remove(record)
                    return True
                else:
                    return False


file_db = 'phone_book.txt'
if not path.exists(file_db):
    with open(file_db, 'w', encoding='utf-8') as _:
        pass

records = []
read_db()
if len(records) != 0:
    i_d = int(records[-1][0]) + 1
else:
    i_d = 0

record_template = {'f_name': '',
               'l_name': '',
               'sur_name': '',
               'phone': ''}


def main():
    choice = ''
    while choice != 'q':
        match choice:
            case '1':
                for _ in records:
                    print(_, end='\n')
                show_menu()
                choice = input()
            case '2':
                find_one()
                show_menu()
                choice = input()
            case '3':
                if add_one():
                    save_db()
                show_menu()
                choice = input()
            case '4':
                if del_one():
                    correct_ids()
                    save_db()
                show_menu()
                choice = input()
            case _:
                print('Wrong input.')
                show_menu()
                choice = input()


main()
