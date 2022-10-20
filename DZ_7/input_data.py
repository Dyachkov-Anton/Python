from work_to_phone_num import chek_valid_num_phone,normalize_num_phone

def choice_menu(choice=20):

    run = True
    while run:
        choice = input("Введите ваш выбор: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                choice = 1
                return choice
            elif choice == 2:
                choice = 2
                return choice
            elif choice == 3:
                choice = 3
                return choice
            elif choice == 4:
                choice = 4
                return choice
            elif choice == 5:
                choice = 5
                return choice
            elif choice == 6:
                return choice
            elif choice ==7:    
                 run = False  # это останавливает цикл while
            else:
                print("Не корректный ввод режима работы")
        else:
            print("Не корректный ввод режима работы")

def input_data():
    ind=True
    while ind:
        num_tel= input("Введите номер телефона:")
        if chek_valid_num_phone(num_tel):
            num_tel=normalize_num_phone(num_tel)
            last_n= input("Введите фамилию:")
            nam = input("Введите Имя:")
            otchest = input("Введите отчество:")
            prim= input("Введите примечание:")
            ind =False
        else:
             print("Вы ввели не корректый номер телефона")
    res=num_tel+" "+last_n+" "+nam+" "+otchest+" "+prim
    return res
    
def input_del_number():
    dell_abonent= input("Введите данные абонента которого вы хотите удалить (Номер телефона или Ф.И.О( или Ф.И...):")
    return dell_abonent 

def input_find_number():
    find_abonent= input("Введите данные абонента которого вы хотите найти (Номер телефона или Ф.И.О( или Ф.И...):")
    return find_abonent 