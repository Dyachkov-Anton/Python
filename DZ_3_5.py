#Задайте число. Составьте список чисел Фибоначчи, 
#в том числе для отрицательных индексов.

#*Пример:*

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 
# 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)

def nego_fib(n):
    nums = []
    num1 = 0
    num2 = 1
    for i in range(n+1):
        nums.append(num1)
        num1, num2 = num2, num1 - num2   
    nums.reverse()
    num1 = 1
    num2 = 1
    for i in range(n):
        nums.append(num1)
        num1, num2 = num2, num1 + num2
    return nums

print(*nego_fib(8))