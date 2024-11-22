import random

def print_board(board: list) -> None:
    '''Печатает доску board'''
    print(board[7], '|', board[8], '|', board[9])
    print('-' * 9)
    print(board[4], '|', board[5], '|', board[6])
    print('-' * 9)
    print(board[1], '|', board[2], '|', board[3])

def get_user_move(board: list) -> int:
    '''Получает ход игрока с проверкой корректности'''
    # Проверить корректность!
    x = int(input('Ваш ход: '))
    return x

def get_computer_move(board: list) -> int:
    '''Получает ход компьютера'''
    return random.randint(1, 9)

def check_win(board: list, tile: str) -> bool:
    '''Проверяет, победил ли игрок, играющий за tile'''
    return False

def check_draw(board: list) -> bool:
    '''Проверяет ничью'''
    return False

board = [' '] * 10

game_on = True
turn = 'компьютер'
while game_on:
    print_board(board)
    print('Ходит', turn)
    if turn == 'компьютер':
        move = get_computer_move(board)
        board[move] = 'x'
        turn = 'человек'
        if check_win(board, 'x'):
            print('Компьютер выиграл.')
            game_on = False
    else:
        move = get_user_move(board)
        board[move] = 'o'
        turn = 'компьютер'
        if check_win(board, 'o'):
            print('Человек выиграл.')
            game_on = False
