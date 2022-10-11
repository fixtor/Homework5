# Создайте программу для игры в ""Крестики-нолики"".


board = list(range(1, 10))

wins = [(1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)]


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
    print('-------------')


def take_input(player_input):
    while True:
        value = input('Выберите куда поставить ' + player_input + ' ? ')
        if not (value in '123456789'):
            print('Ошибка, введите заново')
            continue

        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Занято!')
            continue

        board[value - 1] = player_input
        break


def check_wins():
    for each in wins:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    count = 0
    while True:
        draw_board()
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')

        if count > 3:
            winner = check_wins()
            if winner:
                draw_board()
                print(winner, "Победа")
                break
        count += 1
        if count > 8:
            draw_board()
            print("Ничья")
            break


main()

