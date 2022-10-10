# 1. Вычислить число c заданной точностью d
# 	Пример:	
# 	при d = 0.001, π = 3.141        10-1 <= d <= 10-10

def number_round(in_num,registr):

     c= registr.split('.')
     len_num= len(c[1])
     return round(in_num,len_num)

number=float(input("Введите вещественное число:"))
d=input("Введите точность округления, до знаков:")
print(number_round(number,d))