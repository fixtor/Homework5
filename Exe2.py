# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import *


def user1_move(kandies):

    user1_turn = int(input("ход игрока 1: "))
    flag_user1 = 1

    if user1_turn > 28:
        print('нельзя больше 28!', f'конфет: {kandies}')
        kandies = kandies - 28
    else:
        kandies = kandies - user1_turn
    return kandies


def user2_move(kandies):

    user2_turn = int(input("ход игрока 2: "))
    flag_user2 = 1

    if user2_turn > 28:
       print('нельзя больше 28!', f'конфет: {kandies}')
       kandies -= 28
    else:
       kandies -= user2_turn
    return kandies

def bot_game(kandies):

    if kandies >= 28:
        bot_move = randint(1, 28)
        print(f'Ход бота: {bot_move}')
        kandies = kandies - bot_move
        return kandies
    else:
        bot_move = 28 - 1 #Интеллект, возможность победить при достижении максимального значения ввода
        kandies = kandies - bot_move
        print(f'Ход бота: {bot_move}', f'kandies = {kandies}')

        return kandies

game_kandies = 56
Player1 = 0
Player2 = 0
bot = 0

while game_kandies >= 28:

        game_kandies = user1_move(game_kandies)
        if game_kandies < 0:
            game_kandies = 0

        print(game_kandies)
        Player1 = 1
        Player2 = 0
        bot = 0

        game_kandies = user2_move(game_kandies)
        if game_kandies < 0:
            game_kandies = 0

        print(game_kandies)
        Player1 = 0
        Player2 = 1
        bot = 0

        game_kandies = bot_game(game_kandies)
        if game_kandies < 0:
            game_kandies = 0

        print(game_kandies)

        Player1 = 0
        Player2 = 0
        bot = 1


if bot == 1:
    print('Победил игрок bot')
elif Player1 == 1:
    print(f'Победил игрок 1')
elif Player2 == 1:
    print(f'Победил игрок 2')
