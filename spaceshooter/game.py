import pygame, random

pygame.init()
WIDTH = 480
HEIGHT = 640
INFO_HEIGHT = 50
SCENE_HEIGHT = HEIGHT - INFO_HEIGHT
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Космический шутер')
info = pygame.surface.Surface((WIDTH, INFO_HEIGHT))
scene = pygame.surface.Surface((WIDTH, SCENE_HEIGHT))

clock = pygame.time.Clock()

game_on = True
while game_on:
    # events
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # update
    # render
    info.fill((0, 0, 100))
    scene.fill((0, 0, 0))
    screen.blit(info, (0, 0, WIDTH, INFO_HEIGHT))
    screen.blit(scene, (0, INFO_HEIGHT, WIDTH, HEIGHT))
    pygame.display.flip()

pygame.quit()