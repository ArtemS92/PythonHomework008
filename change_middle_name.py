import json
import contriller

path_to_db = 'db.json'


def change_middle_name():
    name = input(
        'Введите имя и фамилию контакта, фамилию которого будем менять:  ')

    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] and name == data[i]['Surname']:
                data[i]['Middlename'] = input('Новое отчество: ')
            if name not in data:
                print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print('\nОтчество успешно изменено!\n')
    contriller.user_choice()