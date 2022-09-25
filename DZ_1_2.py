#Напишите программу для
# проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

x = int(input("введите х="))
y = int(input("введите y="))
z = int(input("введите z="))


a = not (x or y or z)
b = not x and not y and not z

if a == b:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")