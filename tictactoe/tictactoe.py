import random, time

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
    while True:
        x = input('Ваш ход: ')
        if len(x) != 1:
            print('Нужно ввести один символ - номер клетки')
            continue
        if not x.isdigit():
            print('Ход должен быть цифрой - номером клетки')
            continue
        x = int(x)
        if x < 1 or x > 9:
            print('Номер клетки должен быть от 1 до 9')
            continue
        if board[x] != ' ':
            print('Эта клетка уже занята')
            continue
        return x

def get_computer_move(board: list) -> int:
    '''Получает ход компьютера'''
    legal = [] # список свободных клеток
    for i in range(1, 10):
        if board[i] == ' ':
            legal.append(i)
    # делаем выигрывающий ход, если он возможен
    for x in legal:
        bc = board.copy()
        bc[x] = computer_tile
        if check_win(bc, computer_tile):
            return x
    # делаем блокирующий ход, если человек может выиграть следующим ходом
    if level > 1:
        for x in legal:
            bc = board.copy()
            bc[x] = user_tile
            if check_win(bc, user_tile):
                return x
    # делаем ход в центр, если он свободен
    if level > 2:
        if board[5] == ' ':
            return 5
    # делаем ход в угол, если можно
    if level > 3:
        corners = []
        for i in 1, 3, 7, 9:
            if board[i] == ' ':
                corners.append(i)
        if corners:
            return random.choice(corners)
    # выбираем из оставшихся клеток
    return random.choice(legal)

def check_win(board: list, tile: str) -> bool:
    '''Проверяет, победил ли игрок, играющий за tile'''
    if board[1] == tile and board[4] == tile and board[7] == tile or \
    board[2] == tile and board[5] == tile and board[8] == tile or \
    board[3] == tile and board[6] == tile and board[9] == tile or \
    board[1] == tile and board[2] == tile and board[3] == tile or \
    board[4] == tile and board[5] == tile and board[6] == tile or \
    board[7] == tile and board[8] == tile and board[9] == tile or \
    board[1] == tile and board[5] == tile and board[9] == tile or \
    board[7] == tile and board[5] == tile and board[3] == tile:
        return True
    return False

def check_draw(board: list) -> bool:
    '''Проверяет ничью'''
    return board.count(' ') == 1

board = [' '] * 10

game_on = True
turn = random.choice(['компьютер', 'человек'])

level = int(input('Выберите уровень сложности (1-4): '))

tiles = ['x', 'o']
random.shuffle(tiles)
user_tile, computer_tile = tiles
print('Вы играете за', user_tile)
swap = input('Обменять? (Yes / No) ')
if swap.lower().startswith('y'):
    user_tile, computer_tile = computer_tile, user_tile

while game_on:
    print_board(board)
    time.sleep(2)
    print('Ходит', turn)
    if turn == 'компьютер':
        move = get_computer_move(board)
        board[move] = computer_tile
        turn = 'человек'
        if check_win(board, computer_tile):
            print('Компьютер выиграл.')
            game_on = False
    else:
        move = get_user_move(board)
        board[move] = user_tile
        turn = 'компьютер'
        if check_win(board, user_tile):
            print('Человек выиграл.')
            game_on = False
    if game_on and check_draw(board):
        print('Ничья.')
        game_on = False
print_board(board)