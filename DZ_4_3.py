#Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

import random

def create_random_spisok(num,range_num):
    number=[]
    for i in range(num):
        number.append(random.randint(0,range_num))
    return number

def sort_unical(num,range_num):
    number= create_random_spisok(num,range_num)
    res=[]
    for i in number:
        if number.count(i)==1:
            res.append(i)
    return f'исходный список {number} список неповторяющихся элементов  {res}'

print(sort_unical(11,11))