import json
import contriller

path_to_db = 'db.json'


def delete_contact():
    surname = input('Введите фамилию сотрудника, которого надо удалить: ')
    name = input('Введите имя сотрудника которого надо удалить: ')
    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if surname == data[i]['Surname'] or name == data[i]['Name']:
                del data[i]
            if name and surname not in data:
                print('Такого сотрудника нет')
    with open(path_to_db, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print('\nСотрудник успешно удалён!\n')
    contriller.user_choice()
