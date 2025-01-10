import random


def distance(xa: int, ya: int, xb: int, yb: int) -> int:
    '''Вычисляет расстояние между двумя точками, результат округляется до целого числа'''
    d = ((xa - ya) ** 2 + (ya - yb) ** 2) ** 0.5
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
    if debug_mode:
        for i, j in chests:
            board[i][j] = PRIZE
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
        print(str(i).rjust(2, ' '), *board[i])

def make_chests(cnt: int) -> list:
    '''Прячет на карте cnt сундуков'''
    chests = []
    while len(chests) < cnt:
        chest = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
        if chest not in chests:
            chests.append(chest)
    return chests

WIDTH = 30
HEIGHT = 10
PRIZE = '☠'

board = make_board(WIDTH, HEIGHT)
chests = make_chests(3)
# print(chests)
print_board(board, debug_mode=True)