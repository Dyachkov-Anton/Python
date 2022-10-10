# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num=int(input("Введите натуральное число N: "))

def simple_multiplyers(number):
    multiplyers = []
    mult = 2       
    temp = number 
    while mult * mult <= number:
            if number % mult == 0:
                multiplyers.append(mult)
                number//=mult
            else:
                mult += 1
    multiplyers.append(number)
    return multiplyers 

print(f'список простых множителей числа {num} составляет {simple_multiplyers(num)}')  