from input_data import input_data,input_del_number,input_find_number
from work_to_base import write_base,read_data

def add_phone_record():
    result= input_data()
    write_base(result)

def delete_phone_contact():
    phon_contact=input_del_number()
    baza= read_data()
    for i in baza:
        if phon_contact in i:
            print(f'По заданным критериям найден абонент {i}')
            in_choice= input('Удалить? (да/нет):')
            if in_choice=='да' or 'Да':
                baza.remove(i)
    with open('database.txt', 'w',encoding="utf-8") as file:
        for i in baza:
            file.write(f'{i}')   

def find_phone_contact():
    phon_contact=input_find_number()
    baza= read_data()
    for i in baza:
        if phon_contact in i:
            return print(f'По заданным критериям найден абонент {i}')
    return ("По заданным критериям найден абонент не найден")       