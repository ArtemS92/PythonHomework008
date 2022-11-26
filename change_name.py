import json
import contriller

path_to_db = 'db.json'


def change_name():
    name = input('Введите имя или фамилию контакта, чье имя будем менять:  ')

    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                data[i]['Name'] = input('Новое имя: ')
            if name not in data:
                print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print('\nИмя успешно изменено!\n')
    contriller.user_choice()


