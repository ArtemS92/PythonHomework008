import add_person as ac
import user_interface as ui
import change_name as cn
import change_middle_name as cmn
import change_surname as cs
import delete_person as dc
import view_all_person as vac
import export_in_file as eif
import change_post as cp


def user_choice():
    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 8:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 0:
        ac.create_json()
    elif choice_num == 1:
        ac.add_to_json()
    elif choice_num == 2:
        cn.change_name()
    elif choice_num == 3:
        cmn.change_middle_name()
    elif choice_num == 4:
        cs.change_surname()
    elif choice_num == 5:
        cp.change_post()
    elif choice_num == 6:
        dc.delete_contact()
    elif choice_num == 7:
        vac.view_all_contacts()
    elif choice_num == 8:
        eif.export_txt()
    elif choice_num == 9:
        print('\nСпасибо что пользовались нашим приложением!\n\nДо новых встреч!')
        exit()
