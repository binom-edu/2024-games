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
    print('Привет!')

def get_user_input():
    '''Получает ход игрока с проверкой корректности'''
    pass

def check_move():
    '''Проверяет, отгадана ли буква'''
    pass

def check_win():
    '''Проверка победы игрока'''
    pass

def check_lose():
    '''Проверка поражения игрока'''
    pass

filedir = os.path.dirname(__file__)
fin = open(os.path.join(filedir, 'words.txt'), 'r', encoding='utf8')
words = fin.read().splitlines()
secret = random.choice(words)
print(secret)
wrong = []
correct = []
print_status()