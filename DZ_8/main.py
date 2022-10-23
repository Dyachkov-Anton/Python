from work_base import previev_base,add_record,delete_record,find_record,edit_record,create_base

def input_choice():
    
    while True:

        user_choice= input('''
       _______________________________ 
      |                               | 
      |  1- Просмотреть базу          |
      |  2- Добавить запись           |
      |  3- Удалить запись            | 
      |  4- Найти по Ф.И.О:           | 
      |  5- иИзменить зарплату,премию |
      |  q- Выход                     |
      |_______________________________|
      
      ''')
        if user_choice == "1":
            previev_base()
        elif user_choice == "2":
            add_record()
        elif user_choice == "3":
            delete_record()
        elif user_choice == "4":
            find_record()
        elif user_choice == "5":
            edit_record()    
        elif user_choice.lower() == "q":
            print('Выход')
            break
        else:
            print('Не верно введен режим работы')   
                 
create_base()
input_choice()