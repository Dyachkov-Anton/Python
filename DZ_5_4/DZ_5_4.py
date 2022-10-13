# Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных.

def compres_rle(text):
    result = ''
    pred_simbol = ''
    index = 1
    for char in text:
        if char != pred_simbol:
            if pred_simbol:
                result += str(index) + pred_simbol
            index = 1
            pred_simbol = char
        else:
            index += 1
    else:
        result += str(index)+pred_simbol
    return result

def decompress_text(text):

    result = ''
    index = ''
    for char in text:
        if char.isdigit():
            index += char
        else:
            result += char*int(index)
            index = ''
    return result

with open('not_compres.txt','r') as file:
    not_compres = file.readline()
result_compress= compres_rle(not_compres)    

with open('result_compres.txt', 'w') as file:
    file.write(f'{result_compress}')

with open('compres.txt','r') as file:
     compres = file.readline()
result_decompress= decompress_text(compres)  

with open('decompres.txt', 'w') as file:
     file.write(f'{result_decompress}')