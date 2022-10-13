# Напишите программу, удаляющую из текста все слова, содержащие 
# ""абв"".

def sort_text(text):

    for i in text:
        if "абв" in i:
            text.remove(i)
    list_array = " ".join(text)
    return list_array

all_text = 'абвгде мастер забвение джава'
sort = all_text.split()

print(sort_text(sort))