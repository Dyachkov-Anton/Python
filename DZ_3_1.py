#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной 
# позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
# ответ: 12

spisok= [2, 3, 5, 9, 3]

def summa_negativ_position(array):
    index= len(array)
    result=0
    for i in range(0,index):
        if i%2!=0:
            result+=array[i]
    return result
print (f'сумма элементов списка, стоящих на нечётной позиции: {summa_negativ_position(spisok)}')