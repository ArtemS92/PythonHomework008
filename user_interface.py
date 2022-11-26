import check_number
from export_in_file import export_txt


def start():
    greetings = 'Добро пожаловать в базу данных сотрудников!'
    print(f'{greetings}')


def menu():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    new_book = '0. Создать новую книгу или очистить существующую'
    new_person = '1. Добавить нового сотрудника'
    change_name = '2. Изменить имя'
    change_middle_name = '3. Изменить отчество'
    change_surname = '4. Изменить фамилию'
    change_post = '5. Изменить должность'
    delete_contact = '6. Удалить сотрудника'
    view_all_contact = '7. Показать всех сотрудников'
    export_to_file = '8. Экспортировать данные в файл'
    to_exit = '9. Выход'
    print(
        f'{what_to_do}\n{new_book}\n{new_person}\n{change_name}\n{change_middle_name}\n{change_surname}\n{change_post}\n{delete_contact}\n{view_all_contact}\n{export_to_file}\n{to_exit}')
    return check_number.digit_check()
