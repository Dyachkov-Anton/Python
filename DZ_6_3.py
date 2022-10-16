# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# исходный код
# def create_random_spisok(num,range_num):
#     number=[]
#     for i in range(num):
#         number.append(random.randint(0,range_num))
#     return number

# def sort_unical(num,range_num):
#     number= create_random_spisok(num,range_num)
#     res=[]
#     for i in number:
#         if number.count(i)==1:
#             res.append(i)
#     return f'исходный список {number} список неповторяющихся элементов  {res}'

# print(sort_unical(10,10))

import random
range_num, num = 10, 10
number = [random.randint(0, range_num) for num in range(num)]
sort_unical = [x for x in number if number.count(x) == 1]
print(f'исходный список {number} список неповторяющихся элементов  {sort_unical}')

#2 вариант через lambda и filter

unical= lambda x: number.count(x) == 1
result_list= filter(unical,number)
print(f'исходный список {number} список неповторяющихся элементов  {list(result_list)}')