import json
import contriller


def create_json():
    json_data = []
    with open('db.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    contriller.user_choice()


def add_to_json():
    name = input("Введите Имя: ")
    surname = input('Введите Фамилию: ')
    middle_name = input('Введите Отчество: ')
    post = input('Введите должность: ')
    json_data = {
        "Name": name,
        "Surname": surname,
        "Middlename": middle_name,
        "Post": post,
    }
    data = json.load(open("db.json"))
    data.append(json_data)
    with open("db.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nНовый сотрудник успешно добавлен!\n')
    contriller.user_choice()
