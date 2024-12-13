import random

def make_secret(n: int) -> list:
    '''Создает секретное число длины n'''
    alf = list('0123456789')
    while alf[0] == '0':
        random.shuffle(alf)
    return ''.join(alf[:n])
    # secret = ''
    # for i in range(n):
    #     while True:
    #         d = random.choice(alf)
    #         if d in secret:
    #             continue
    #         if i == 0 and d == '0':
    #             continue
    #         secret += d
    #         break
    # return secret

def check_answer(guess: str) -> dict:
    res = {
        'bulls': 0,
        'cows': 0
    }
    for i in range(n):
        if guess[i] == secret[i]:
            res['bulls'] += 1
        elif guess[i] in secret:
            res['cows'] += 1
    return res
    
n = int(input('Укажите уровень сложности (3-10): '))
secret = make_secret(n)

game_on = True
while game_on:
    guess = input('Ваше число: ')
    res = check_answer(guess)
    print('Быки:', res['bulls'])
    print('Коровы:', res['cows'])
    if res['bulls'] == n:
        print('Число отгадано!')
        game_on = False