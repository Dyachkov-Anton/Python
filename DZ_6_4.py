# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# spisok = []
# for i in range(0, 21):
#     spisok.append(random.randint(1, 100))

# def sort(array):
#     res = []
#     res2=[]
#     for i in array:
#         if i % 2 == 0:
#             res.append(i)
#         else:
#             res2.append(i)    
#     
#     res.extend(res2)
#     return res

# print(f' список до сортировки {spisok}')
# print(f' список после сортировки {sort(spisok)}')

import random
spisok= [random.randint(0,100) for num in range(21)]
even = lambda x: x % 2 == 0
non_even= lambda x: x % 2 != 0

even_list=filter(even,spisok) 
not_even=filter(non_even,spisok)
 
even_res= list(even_list)
not_even_res =list(not_even)
even_res.extend(not_even_res)

print (f'список до    сортировки {spisok}')
print (f'список после сортировки {even_res}')

# 2 вариант

even_res1 =[x for x in spisok if x % 2 == 0]  
not_even1 =[x for x in spisok if x % 2 != 0]
even_res1.extend(not_even1)

print("Второй вариант")
print (f'список до сортировки {spisok}')
print (f'список после сортировки {even_res1}')