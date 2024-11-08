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
    alf = 'аб'
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
wrong = []
correct = []

# удалить после отладки
secret = 'таракан'
wrong = ['ш', 'б']
correct = ['а', 'н']
# удалить после отладки

print_status()