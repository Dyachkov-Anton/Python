#Напишите программу, которая будет преобразовывать десятичное 
# число в двоичное.
#*Пример:*
#45 -> 101101
#3 -> 11
#2 -> 10

def dex_to_bin(num):
    res=""     
    while num>0:
        res = str(num%2)+res
        num=num//2
    return res
number = int(input("Введите число:"))

print(f'Число {number} в двоичной системе: {dex_to_bin(number)}')