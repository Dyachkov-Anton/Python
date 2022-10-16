# Задача: предложить улучшения кода для уже решённых задач:
# Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".
# def sort_text(array):

#     for i in array:
#         if "абв" in i:
#             array.remove(i)
#     list_array = " ".join(array)
#     return list_array

# sa = 'абвгдейка кинотеатр забвеность питон забвение прикол абвер'
# sort1 = sa.split()
# print(sort_text(sort1))

stroka = 'абвгдейка кинотеатр забвеность питон забвение прикол абвер'
sorted_list = [x for x in stroka.split() if "абв" not in x]
list_sorted = " ".join(sorted_list)
print(list_sorted)