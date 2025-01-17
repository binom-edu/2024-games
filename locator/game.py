import random, copy


def distance(xa: int, ya: int, xb: int, yb: int) -> int:
    '''Вычисляет расстояние между двумя точками, результат округляется до целого числа'''
    d = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
    return round(d)

def make_board(width: int, height: int) -> list:
    alf = '~-,'
    res = []
    for i in range(height):
        line = []
        for j in range(width):
            line.append(random.choice(alf))
        res.append(line)
    return res

def print_board(board: list, debug_mode=False) -> None:
    bc = copy.deepcopy(board)
    if debug_mode:
        for i, j in chests:
            bc[i][j] = PRIZE
    print('   ', end='')
    for x in range(WIDTH):
        if x % 10 == 0:
            print(x // 10, end=' ')
        else:
            print(' ', end=' ')
    print()
    print('   ', end='')
    for x in range(WIDTH):
        print(x % 10, end=' ')
    print()
    for i in range(HEIGHT):
        print(str(i).rjust(2, ' '), *bc[i])

def make_chests(cnt: int) -> list:
    '''Прячет на карте cnt сундуков'''
    chests = []
    while len(chests) < cnt:
        chest = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
        if chest not in chests:
            chests.append(chest)
    return chests

def get_user_input():
    print('Укажите точку на карте (сперва номер строки, потом номер столбца, через пробел)')
    i, j = map(int, input().split())
    return i, j

def get_min_dist(i: int, j: int) -> int:
    d = []
    for x, y in chests:
        d.append(distance(i, j, x, y))
    return min(d)


WIDTH = 30
HEIGHT = 10
PRIZE = '☠'

board = make_board(WIDTH, HEIGHT)
chests = make_chests(3)
print_board(board, debug_mode=True)
print_board(board, debug_mode=False)

print('Тут правила игры')
game_on = True
while game_on:
    print_board(board)
    print('Осталось сундуков:', len(chests))
    i, j = get_user_input()
    d = get_min_dist(i, j)
    if d == 0:
        print('Поздравляем! Вы нашли сундук!')
        board[i][j] = PRIZE
        chests.remove((i, j))
        if len(chests) == 0:
            print('Игра окончена.')
            print_board(board)
            game_on = False
    elif d < 10:
        print('До ближайшего сундука:', d)
        board[i][j] = str(d)
    else:
        print('Ничего поблизости не найдено')
        board[i][j] = 'X'