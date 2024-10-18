import random

max_attempts = 8

secret = random.randint(1, 100)
print(f'Компьютер загадал число от 1 до 100. Вам предстоит его угадать, используя не более {max_attempts} попыток.')
attempt = 1

gameOn = True
while gameOn:
    print('Попытка №', attempt)
    userChoice = input()
    if userChoice.isdigit():
        userChoice = int(userChoice)
    else:
        print('Нужно ввести число!')
        continue
    if userChoice == secret:
        print(f'Поздравляем! Вы отгадали число за {attempt} попыток!')
        gameOn = False
    if userChoice < secret:
        print('Загаданное число больше.')
    if userChoice > secret:
        print('Загаданное число меньше.')
    attempt = attempt + 1
    if attempt > max_attempts:
        print(f'Вы израсходовали все попытки. Было загадано число {secret}')
        gameOn = False
print('Игра окончена.')