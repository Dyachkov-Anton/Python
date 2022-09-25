#Найти расстояние между двумя 
# точками пространства.

x_coord = float(input("введите координату первого числа х="))
y_coord = float(input("введите координату первого числа у="))
x_coord2 = float(input("введите координату второго числа х="))
y_coord2 = float(input("введите координату второго числа у="))

def lens(x1, y1, x2, y2):
    res = round(((x2 - x1) ** 2 + ((y2 - y1)) ** 2) ** 0.5, 2)
    return res

result = lens(x_coord, y_coord, x_coord2, y_coord2)

print(result)