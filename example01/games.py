# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 28:
        return True
    else:
        return False


def stp(player, count, m_c):
    proccess = True
    win_player = ''
    candy = count
    k = input(f'{player} ходит,  введите число от 1 до {m_c}:')
    invalid = True
    while invalid:
        if is_valid(k):
            candy -= int(k)
            invalid = False
            if candy <= 0:
                win_player = player
                proccess = False
    return candy, proccess, win_player


def bot(count, m_c):
    proccess = True
    win_player = ''
    candy = count
    x = count % m_c
    if x != 0:
        if (candy - x) > m_c and (candy - m_c) > m_c:
            candy -= x
            print(f'Бот Вася взял {x} конфет')
        elif 0 < candy <= m_c:
            l = candy
            candy -= candy
            print(f'Бот Вася взял {l} конфет')
        else:
            candy -= 1
            print(f'Бот Вася взял {1} конфет')
    else:
        if (candy - x) > m_c and (candy - m_c) > m_c:
            candy -= m_c
            print(f'Бот Вася взял {m_c} конфет')
        elif 0 < candy <= m_c:
            l = candy
            candy -= candy
            print(f'Бот Вася взял {l} конфет')
        else:
            candy -= 1
            print(f'Бот Вася взял {1} конфет')
    if candy <= 0:
        win_player = 'Bot is won'
        proccess = False

    return candy, proccess, win_player


def procces(p1, p2, all_canndy, f_m, m_c, mode):
    candy = all_canndy
    proccess = True
    step = 0
    win_player = ''

    if p1 == f_m:
        player = p1
        player2 = p2
        cpu = 2
    else:
        player = p2
        player2 = p1
        cpu = 1

    if mode == '1':
        while proccess:
            print(f'Конфет осталось {candy}')
            if step == 0:
                s = stp(player, candy, m_c)
                candy = s[0]
                proccess = s[1]
                win_player = s[2]
                if step == 1:
                    step = 0
                else:
                    step = 1
            else:
                s = stp(player2, candy, m_c)
                candy = s[0]
                proccess = s[1]
                win_player = s[2]
                if step == 1:
                    step = 0
                else:
                    step = 1
    else:
        while proccess:
            print(f'Конфет осталось {candy}')
            if step == 0:
                if cpu == '2' or cpu == 2:
                    s = bot(candy, m_c)
                else:
                    s = stp(player2, candy, m_c)
                candy = s[0]
                proccess = s[1]
                win_player = s[2]
                if step == 1:
                    step = 0
                else:
                    step = 1
            else:
                if cpu == '1' or cpu == 1:
                    s = bot(candy, m_c)
                else:
                    s = stp(player, candy, m_c)
                candy = s[0]
                proccess = s[1]
                win_player = s[2]
                if step == 1:
                    step = 0
                else:
                    step = 1
    return win_player


def init_game(p1, p2, mode='1'):

    player_1 = p1
    player_2 = p2
    all_canndy = 100 #2100
    f_move = random.choice((player_1, player_2))
    max_canndy = 28

    return player_1, player_2, all_canndy, f_move, max_canndy, mode


print('Добро пожаловать')

flag = True
while flag:
    mode = input('Вы хотите играть с другом или ботом 1/2')

    if mode == '1' or mode == 1:
        p1 = input('Player 1')
        p2 = input('Player 2')
        game = init_game(p1, p2, str(mode))
        flag = False
    elif mode == '2' or mode == 2:
        p1 = input('Player 1')
        p2 = 'Bot_Vasya'
        game = init_game(p1, p2, str(mode))
        flag = False
    else:
        print('Введите коректный режим игры')

    game_process = True

    while game_process:
        game_process = procces(game[0], game[1], game[2], game[3], game[4], game[5])
        print(f'Победил игрок {game_process}')

        q = input(f'Хотите еще сыграть ? y/n')
        if q == 'y':
            pass
        else:
            game_process = False