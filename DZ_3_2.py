# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний 
# и т.д.
# *Пример:*
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

def first_end_ellem(array):
    index= len(array)-1
    result=[]
    res=1
    index= index//2
    print(index)
    for i in range(index+1):
        res=array[i]*array[(i+1)*-1]
        result.append(res)
    return result    
spisok =[2, 3, 4, 5, 6] # 12 15 16
spisok2 =[2, 3, 5, 6]   # 12 15

print(first_end_ellem(spisok)) 
print(first_end_ellem(spisok2)) 