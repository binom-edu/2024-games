import random, os

frames = [
'''
-------||
  |    ||
       ||
       ||
       ||
       ||
==========
''',
'''
-------||
  |    ||
  o    ||
       ||
       ||
       ||
==========
''',
'''
-------||
  |    ||
  o    ||
  0    ||
       ||
       ||
==========
''',
'''
-------||
  |    ||
  o    ||
 /0    ||
       ||
       ||
==========
''',
'''
-------||
  |    ||
  o    ||
 /0\\   ||
       ||
       ||
==========
''',
'''
-------||
  |    ||
  o    ||
 /0\\   ||
 /     ||
       ||
==========
''',
'''
-------||
  |    ||
  o    ||
 /0\\   ||
 / \\   ||
       ||
==========
''',
]

def print_status():
    '''Выводит на экран состояние игры'''
    print('Ход', len(wrong) + len(correct) + 1)
    for i in secret:
        if i in correct:
            print(i, end=' ')
        else:
            print('-', end=' ')
    print()
    print('Ошибки:', *wrong)
    print(frames[len(wrong)])

def get_user_input():
    '''Получает ход игрока с проверкой корректности'''
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыь'
    while True:
        s = input('Введите букву: ').lower()
        if len(s) != 1:
            print('Нужно ввести ровно одну букву!')
            continue # пропустить остальные команды и вернуться в начало цикла
        if s not in alf:
            print('Слово состоит только из русских букв.')
            continue
        if s in wrong or s in correct:
            print('Эта буква уже использована!')
            continue
        return s

def check_move(s):
    '''Проверяет, отгадана ли буква'''
    return s in secret

def check_win():
    '''Проверка победы игрока'''
    for s in secret:
        if s not in correct:
            return False
    return True

def check_lose():
    '''Проверка поражения игрока'''
    return len(wrong) == len(frames) - 1

filedir = os.path.dirname(__file__)
fin = open(os.path.join(filedir, 'words.txt'), 'r', encoding='utf8')
words = fin.read().splitlines()
secret = random.choice(words)
wrong = []
correct = []

print('Вот тут вот правила игры')

game_on = True
while game_on:
    print_status()
    x = get_user_input()
    if check_move(x):
        print('Буква отгадана!')
        correct.append(x)
    else:
        print('Такой буквы нет в слове.')
        wrong.append(x)
    if check_win():
        print('Вы победили!')
        game_on = False
    if check_lose():
        print('Вы проиграли! Было загадано слово', secret)
        game_on = False
        print(frames[-1])
