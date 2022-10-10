#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file_result.txt','r') as file:
    multi = file.readline()
   

with open('file_result2.txt','r') as file:
    multi2 = file.readline()
   

modifi_multi=multi[:-3].replace('x^2','').replace('x',"").split("+")
modifi_multi2=multi2[:-3].replace('x^2','').replace('x',"").split("+")
 

result=f' {int(modifi_multi[0])+int(modifi_multi2[0])}x^2+{int(modifi_multi[1])+int(modifi_multi2[1])}x+{int(modifi_multi[2])+int(modifi_multi2[2])} =0'


with open('sum_multi.txt', 'a') as file:
    file.write(f'{result}')