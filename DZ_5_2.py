# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. 
# се конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать 
# все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def input_num_candy(candy_qu):
    num = (input("Введите количество конфет, которые вы хотите взять: "))
    if num.isdigit():
        num = int(num)
        if num > candy_qu:
            print(f"нельзя взять конфет больше 28 и больще, чем осталось. Всего осталось {candy_qu} конфет")
            return input_num_candy(candy_qu)
        elif num > 28:
            print("Вы взяли  больше 28 конфет. Так нельзя - возмите заново")
            return input_num_candy(candy_qu)
        elif num == 0:
            print("Ну возмите хоть одну конфетку")
            return input_num_candy(candy_qu)
        else:
            return num
    else:
        print("Нужно ввести целое число, половинки тоже не даем !!!")
        return input_num_candy(candy_qu)

def bot_motion(candy_qu):
    if candy_qu > 80:
        res = random.randint(1, 29)
        return res
    elif candy_qu <= 28:
        res = candy_qu
        return res
    else:
        atemp = candy_qu//28
        if atemp == 1:
            f = candy_qu 
            temp = f
            while f >= 29:
                res = temp-29
                f -= 1
                if res == 0: 
                    res += 1
            return res

        res = candy_qu-(atemp)*28+1

    return res

def main_game(bot=False):

    print("Начинаем игру с конфетами 2021 \nДавайте представимся")

    Name_player1 = input("Введите имя первого игрока: ")
    if bot:
        Name_player2 = "Bot"
    else:
        Name_player2 = input("Введите имя второго игрока: ")
    print(f'\nиграет игрок №1 {Name_player1} против игрока №2 {Name_player2}')
    print(f"\nНапоминаем правила игры -нужно брать конфеты, за один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход")
    one_player = ''
    two_player = ''
    print(f"\nтеперь определим кто ходит первым")
    i=random.randint(1,2)
    if i==1:
        one_player,two_player= Name_player1,Name_player2
    else:
        one_player,two_player= Name_player2,Name_player1
    
    print(f'\nПо результам жеребьевки первым ходит игрок {one_player}')

    candy_quant = 120                                                            
    allcandy_first = 0
    allcandy_second = 0
    last_player1 = 0                                                           
    
    print(f'Всего конфет: {candy_quant}')
    while candy_quant > 0:

        print(f'ходит игрок {one_player} ')
        if one_player == "Bot":
            first = int(bot_motion(candy_quant))
        else:
            first = int(input_num_candy(candy_quant))
        allcandy_first += first
        candy_quant -= first
        last_player1 = 1
        print(f'осталось {candy_quant}')
        if candy_quant > 0:
            if two_player == "Bot":
                second = int(bot_motion(candy_quant))
            else:
                second = int(input_num_candy(candy_quant))
            print(f'ходит игрок {two_player} и взял  {second} конфет')
            candy_quant -= second
            allcandy_second += second
            last_player1 = 0
        print(f'осталось {candy_quant}')

    print(f'В итоге : конфет у {one_player}  {allcandy_first}  конфет у {two_player}   {allcandy_second}')
    if last_player1 == 1:
        print(f'Так как последним забрал конфеты игрок {one_player}, то он выиграл и забрал все конфеты')
    else:
        print(f'Так как последним забрал конфеты игрок {two_player}, то он выиграл и забрал все конфеты')


bot_or_humans = input("Будем играть с ботом? Введите да иначе играют 2 игрока: ")

if bot_or_humans.lower() == "да":

    main_game(True)                  
else:
    main_game()