#Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов 
# на указанных позициях. Позиции хранятся в списке 
# positions - создайте этот список 
# (например:positions = [1, 3, 6]).


def new_spisok(num, p1, p2, p3):
    res = []
    poz = [p1, p2, p3]
    result = 1
    for i in range(-num, num+1):
        res.append(i)
    maxindex = len(res)-1
    minidex = len(res)
    for n in poz:
        if n > maxindex or n < -minidex:
            return print("неверно указали значение индекса ")
        result *= res[n]
    return print(f' В списке {res}, произведение значений с индексами {p1},{p2},{p3} составляет {result}')


number = int(input("Введите  число N:  "))

poz1 = int(input("Введите  индекс первого числа  числа : "))
poz2 = int(input("Введите  индекс  второго числа  числа : "))
poz3 = int(input("Введите  индекс  третьего числа  числа : "))

new_spisok(number, poz1, poz2, poz3)