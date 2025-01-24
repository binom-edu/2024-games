import pygame

pygame.init()
screen = pygame.display.set_mode((300, 400), 0, 32)
pygame.display.set_caption('Без имени-1')
clock = pygame.time.Clock()

FPS = 30

game_on = True
while game_on:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # обновление
    # отрисовка

pygame.quit()