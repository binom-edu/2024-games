import pygame
import random

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.image.fill((255, 0, 0))
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vx = (random.random() - 0.5) * 10
        self.vy = (random.random() - 0.5) * 10

    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy = -self.vy
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vx = -self.vx

WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Без имени-1')
clock = pygame.time.Clock()

FPS = 60

hero = Hero()


game_on = True
while game_on:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # обновление
    hero.update()
    # отрисовка
    screen.fill((0, 0, 0))
    screen.blit(hero.image, hero.rect)
    pygame.display.flip()

pygame.quit()