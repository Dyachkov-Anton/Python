#Вывести на экран числа от -N до N.
#num=int(input("Add -N: "))
#NUM=int(input("Add N: "))
#while (num<=NUM):
#    print(f"{num} ")
#    num=num+1

#Вывести на экран числа от -N до N.

num = int(input("Введите целое число: "))

def print_num(number):
    number= abs(number)
    first= number*-1
    second= number
    while first <=second:
        print(f' {first},',end='')
        first+=1

print_num(num)    