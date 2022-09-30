#Написать программу получающую набор произведений чисел от 1 до N.

N = int(input("Введите  число N:  "))  


def res_N(num):
    res = 1
    multi = []
    for i in range(1, num+1):
        res *= i
        multi.append(res)
    return multi


print(res_N(N))