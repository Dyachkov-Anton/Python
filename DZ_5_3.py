# Создайте программу для игры в ""Крестики-нолики"".

pole = [0] * 3                       
for i in range(3):
    pole[i] = [0] * 3
    index = 1
for i in range(3):
    for j in range(3):
        pole[i][j] = f'__{index}__'
        index += 1


def print_field(pole):          # печать поля

    for i in range(3):
        print(pole[i])


def input_field_num(player_num, pol):                                 

    num = (input("Введите номер поля :"))
    if num.isdigit():                                                       
      num = int(num)
      if num < 1 or num > 9:
          print(f"введите корректное значение позиции от 1 до 9")
          input_field_num(player_num, pol)
      if player_num == 1:
          temp = "__X__"
      else:
          temp = "__0__"
      if num < 4:
          if pol[0][num-1] == "__X__" or pol[0][num-1] == "__0__":
              print(f'ячейка с номером {num} занята, повторите ввод ')
              input_field_num(player_num, pol)
          else:
              pol[0][num-1] = temp
      elif num > 3 and num < 7:
          if pol[1][num-4] == "__X__" or pol[1][num-4] == "__0__":
              print(f'ячейка с номером {num} занята, повторите ввод ')
              input_field_num(player_num, pol)
          else:
              pol[1][num-4] = temp
      elif num> 6 and num < 10:
          if pol[2][num-7] == "__X__" or pol[2][num-7] == "__0__":
              print(f'ячейка с номером {num} занята,  ввод ')
              input_field_num(player_num, pol)
          else:
              pol[2][num-7] = temp
      return pol        
    else:
       print(f"не корректный ввод, повторите")
       input_field_num(player_num, pol)        
    




def check_win(pol):                                 # проверка на победу
    for i in range(len(pol)):
        if pol[i][0] == pol[i][1] == pol[i][2]:
            return True
        if pol[0][i] == pol[1][i] == pol[2][i]:
            return True
    if  pol[0][0] == pol[1][1] == pol[2][2]:
            return True
    if  pol[0][2] == pol[1][1] == pol[2][0]:
            return True                  
    else: return False


def main_game(pol):
  count=1                 
  n=1                         # определяет номер игрока
  while count <=9:

    print_field(pole)
    if count%2 !=0:
      n=1
      print("Ходит крестик")
      input_field_num(n, pole)
      if check_win(pol):
        print("Поздравляю!! Выиграл крестик")
        print_field(pole)
        break
    else:
      n=2
      print("Ходит нолик")  
      input_field_num(n, pole)
      if check_win(pol):
        print("Поздравляю!! Выиграл нолик")
        print_field(pole)
        break
    if count==9:
      print("Боевая ничья")
      print_field(pole)
    count+=1  



main_game(pole)