def read_data():
     with open('database.txt','r',encoding="utf-8") as file:
        data = file.readlines()
        data_phone=[]
        for line in data:
            data_phone.append(line)
        return data_phone

def write_base(data):

    with open('database.txt', 'a',encoding="utf-8") as file:
     file.write(f'{data}\n')
        
def export_to_csv():
    baza= read_data()
    with open('export.csv', 'w',encoding="utf-8") as file:
        for i in baza:
            file.write(f'{i}')
    print("Экспорт завершен") 