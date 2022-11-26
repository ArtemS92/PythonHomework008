import json

import contriller

path_to_db = 'db.json'


def change_post():
    name = input('Введите имя или фамилию контакта, чью должность будем менять:  ')

    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Post'] = input('Новая должность: ')
            if name not in data:
                print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print('\nДолжность успешно изменена!\n')
    contriller.user_choice()
