#Показать первую цифру дробной части числа.
num = float(input("Введите дробное число: "))

round_num = int(num) # 5

result = (num-round_num)*10 # 7.7

print(f' первая цифра дробной части: {int(result)}')

