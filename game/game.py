import pygame
import random

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((5, 5))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, (255, 255, 255), (2, 2), 2)
        self.rect.x = random.randint(0, WIDTH - 1)
        self.rect.y = random.randint(0, HEIGHT - 1)
        self.vx = (random.random() - 0.5) * 2
        self.vy = (random.random() - 0.5) * 2
        all_sprites.add(self)

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
all_sprites = pygame.sprite.Group()

n = 30
heroes = []
for i in range(n):
    heroes.append(Hero())

game_on = True
while game_on:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # обновление
    all_sprites.update()
    # отрисовка
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    for i in range(n - 1):
        for j in range(i + 1, n):
            x1, y1 = heroes[i].rect.center
            x2, y2 = heroes[j].rect.center
            d = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if d <= 10000:
                k = 255 * d // 10000
                pygame.draw.line(screen, (255-k, 255-k, 255-k), (x1, y1), (x2, y2))

    pygame.display.flip()

pygame.quit()