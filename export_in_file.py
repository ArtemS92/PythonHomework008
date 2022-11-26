import json
import contriller

path_to_db = 'db.json'


def export_txt():
    name = input('Введите имя, фамилию или должность сотрудника, для экспорта в файл:  ')

    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname'] or name == data[i]['Post']:
                with open('Export_person.txt', 'a') as export:
                    export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
                        data[i]['Middlename']) + ' ' + "".join(data[i]['Surname']) + ' ' + "".join(data[i]['Post']))

    print('\nДанные успешно экспортированы в файл!\n')
    contriller.user_choice()
