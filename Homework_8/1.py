# -*- coding: utf-8 -*-

from os import path

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных

"""
Description:
    This script is a simple phone book. It has functionality for adding,
    deleting, editing and searching records. Records are of the type:
    'id FirstName LastName SurName Phone' (defined in the structure
    record_template). The record ID starts with 1. Records are read and saved in
    a text file (file_db).
"""


def action():
    print("1) Показать книгу.\t"
          "2) Найти человека.\n"
          "3) Добавить человека.\t"
          "4) Удалить человека.\n"
          "5) Редактировать запись.\t"
          "6) Обновить данные.\n"
          "Для выхода введите 'q'.")
    return input()


def load_db():
    global file_db
    global records
    global i_d

    with open(file_db, 'r') as f:
        for line in f.readlines():
            records.append(line.rstrip('\n'))
    print('Data updated')
    if len(records) != 0:
        i_d = int(records[-1].split()[0]) + 1


def save_db():
    global file_db
    global records

    with open(file_db, 'w', encoding='utf-8') as f:
        for i in records:
            f.write(i + '\n')
    print('Phonebook saved.')


def reset_records():
    global records
    global i_d

    records.clear()
    i_d = 1


def find_one():
    global records

    member = input('Введите имя, фамилию, или id человека из книги ')
    for i in range(len(records)):
        selection = records[i].split()
        for j in selection:
            if member == j:
                identifier = int(selection[0])
                print(records[i])
                return identifier
    print('Такой записи нет в книге.')
    return None


def get_new_one():
    global record_template

    for key in record_template.keys():
        record_template[key] = input(f"{key} ")
    return ' '.join(record_template.values())


def edit_one():
    global records

    one = find_one()
    if one:
        records[one - 1] = str(one) + ' ' + get_new_one()


def add_one():
    global records
    global i_d

    one = get_new_one()
    for record in records:
        if one == record[2:]:
            print('Невозможно добавить запись. Данная запись уже существует.')
            return False
    records.append(f"{i_d} {one}")
    i_d += 1
    return True


def del_one():
    global records

    member = input('Введите имя, фамилию, id, или телефон человека из книги ')
    for record in records:
        for i in record.split():
            if member == i:
                print(f"Чтобы удалить эту запись нажмите 'Enter'\n{record}")
                if input() == '':
                    records.remove(record)
                    return True
                else:
                    return False


def correct_ids():
    global records
    count = 1

    for i in range(len(records)):
        records[i] = str(count) + ' ' + ' '.join(records[i].split()[1:])
        count += 1


def main():
    choice = ''
    while choice != 'q':
        match choice:
            case '1':
                for _ in records:
                    print(_, end='\n')
                choice = action()
            case '2':
                find_one()
                choice = action()
            case '3':
                if add_one():
                    save_db()
                choice = action()
            case '4':
                if del_one():
                    correct_ids()
                    save_db()
                choice = action()
            case '5':
                edit_one()
                save_db()
                choice = action()
            case '6':
                reset_records()
                load_db()
                choice = action()
            case _:
                choice = action()


file_db = 'phone_book.txt'
records = []
i_d = 1
record_template = {'f_name': '',
                   'l_name': '',
                   'sur_name': '',
                   'phone': ''}

if not path.exists(file_db):
    with open(file_db, 'w', encoding='utf-8') as _:
        pass
load_db()


main()
