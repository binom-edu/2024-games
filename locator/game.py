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

def print_board(board: list) -> None:
    for line in board:
        print(*line)

WIDTH = 30
HEIGHT = 10

board = make_board(WIDTH, HEIGHT)
print_board(board)