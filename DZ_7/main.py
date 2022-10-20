from out_display import print_all_base, print_menu,viev_help
from input_data import choice_menu
from operating_mode import add_phone_record, delete_phone_contact,find_phone_contact 
from work_to_base import export_to_csv

run=True

while run:
    print_menu()
    choice= choice_menu()
    if choice==1:
        add_phone_record()
    elif choice == 2:
        delete_phone_contact()
    elif choice == 3:
        find_phone_contact()
    elif choice == 4:
        export_to_csv()
    elif choice == 5:
        print_all_base()
    elif choice == 6:
        viev_help()
    elif choice == None:
        run= False

# choice= choice_menu()
# print(choice)