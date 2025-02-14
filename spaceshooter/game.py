import pygame, random, os

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'hero.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = SCENE_HEIGHT - 20
        all_sprites.add(self)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.rect.x += 2
            if self.rect.right > WIDTH - 1:
                self.rect.right = WIDTH - 1
        if pressed[pygame.K_LEFT]:
            self.rect.x -= 2
            if self.rect.left < 0:
                self.rect.left = 0

pygame.init()
WIDTH = 480
HEIGHT = 640
INFO_HEIGHT = 50
SCENE_HEIGHT = HEIGHT - INFO_HEIGHT
FPS = 60
DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(DIR, 'img')

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Космический шутер')
info = pygame.surface.Surface((WIDTH, INFO_HEIGHT))
scene = pygame.surface.Surface((WIDTH, SCENE_HEIGHT))

all_sprites = pygame.sprite.Group()
hero = Hero()

clock = pygame.time.Clock()

game_on = True
while game_on:
    # events
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # update
    all_sprites.update()
    # render
    info.fill((0, 0, 100))
    scene.fill((0, 0, 0))
    all_sprites.draw(scene)
    screen.blit(info, (0, 0, WIDTH, INFO_HEIGHT))
    screen.blit(scene, (0, INFO_HEIGHT, WIDTH, HEIGHT))
    pygame.display.flip()

pygame.quit()