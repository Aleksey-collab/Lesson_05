# 2. Создайте программу для игры в ""Крестики-нолики"".

def print_desk(game_desk):
    print(*[i for i in game_desk], sep='\n')

def is_valid(y, x, game_desk, sign):
    game_process = True
    win_player = sign
    flag = True
    while flag:
        if 0 <= y <= 2 and 0 <= x <= 2:
            if game_desk[y][x] == '*':
                game_desk[y][x] = sign
                flag = False
            else:
                print('поле занято, попробуйте в другую клетку')
                y = int(input('Введите y координат'))
                x = int(input('Введите х координат'))
        else:
            print('введите корректные координаты от 0 до 2')
            y = int(input('Введите y координат'))
            x = int(input('Введите х координат'))

    # X valid
    if game_desk[0][0] == 'X' and game_desk[0][1] == 'X' and game_desk[0][2] == 'X':
        print('Победили X')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][0] == 'X' and game_desk[1][0] == 'X' and game_desk[2][0] == 'X':
        print('Победили X')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][0] == 'X' and game_desk[1][1] == 'X' and game_desk[2][2] == 'X':
        print('Победили X')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][1] == 'X' and game_desk[1][1] == 'X' and game_desk[2][1] == 'X':
        print('Победили X')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][2] == 'X' and game_desk[1][2] == 'X' and game_desk[2][2] == 'X':
        print('Победили X')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][2] == 'X' and game_desk[1][1] == 'X' and game_desk[2][0] == 'X':
        print('Победили X')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[1][0] == 'X' and game_desk[1][1] == 'X' and game_desk[1][2] == 'X':
        print('Победили X')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[2][0] == 'X' and game_desk[2][1] == 'X' and game_desk[2][2] == 'X':
        print('Победили X')
        game_process = False
        return game_desk, game_process, win_player

    # 0 valid
    if game_desk[0][0] == '0' and game_desk[0][1] == '0' and game_desk[0][2] == '0':
        print('Победили 0')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][0] == '0' and game_desk[1][0] == '0' and game_desk[2][0] == '0':
        print('Победили 0')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][0] == '0' and game_desk[1][1] == '0' and game_desk[2][2] == '0':
        print('Победили 0')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][1] == '0' and game_desk[1][1] == '0' and game_desk[2][1] == '0':
        print('Победили 0')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][2] == '0' and game_desk[1][2] == '0' and game_desk[2][2] == '0':
        print('Победили 0')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[0][2] == '0' and game_desk[1][1] == '0' and game_desk[2][0] == '0':
        print('Победили 0')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[1][0] == '0' and game_desk[1][1] == '0' and game_desk[1][2] == '0':
        print('Победили 0')
        game_process = False
        return game_desk, game_process, win_player
    elif game_desk[2][0] == '0' and game_desk[2][1] == '0' and game_desk[2][2] == '0':
        print('Победили 0')
        game_process = False
        return game_desk, game_process, win_player
    elif "*" not in game_desk[0] and "*" not in game_desk[1] and "*" not in game_desk[2]:
        print('Ничья')
        game_process = False
        return game_desk, game_process

    return game_desk, game_process


desk = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
s = ''

print_desk(desk)

in_game = True
i = 0
while in_game:
    if i % 2 == 0:
        print('Player 1')
        s = '0'
        coord_y = int(input('Введите y координат'))
        coord_x = int(input('Введите х координат'))
        process = is_valid(coord_y, coord_x, desk, s)
        desk = process[0]
        print_desk(desk)
        in_game = process[1]
        if len(process) == 3:
            print('Победил Player 1 "0"')
    else:
        print('Player 2')
        s = 'X'
        coord_y = int(input('Введите y координат'))
        coord_x = int(input('Введите х координат'))
        process = is_valid(coord_y, coord_x, desk, s)
        desk = process[0]
        print_desk(desk)
        in_game = process[1]
        if len(process) == 3:
            print('Победил Player 2 "0"')

    i += 1
