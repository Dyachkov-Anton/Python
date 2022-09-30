## Задать список из n чисел последовательности  (1 + 1/n)^n и
# вывести на экран их сумму.

n = int(input("Введите  число n:  "))

def list_numbers(n):
    res = []
    for n in range(1, n+1):
        form = (1 + 1/n)**n
        res.append(form)
    return res
print(list_numbers(n))
print(sum(list_numbers(n)))