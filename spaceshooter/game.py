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

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = random.choice(['small', 'middle', 'big'])
        path = os.path.join(IMG_DIR, 'mobs', self.size)
        filenames = os.listdir(path)
        self.image = pygame.image.load(
            os.path.join(path, random.choice(filenames))
        ).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(-100, WIDTH + 100),
            random.randint(-400, -100)
        )
        self.vx = random.randint(-2, 2)
        self.vy = random.randint(1, 5)
        self.vr = random.randint(-3, 3)
        self.angle = 0
        all_sprites.add(self)
        mobs.add(self)
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top > SCENE_HEIGHT:
            self.rect.center = (
                random.randint(-100, WIDTH + 100),
                random.randint(-400, -100)
            )
        # self.angle = (self.angle + self.vr) % 360
        # self.image = pygame.transform.rotate(self.image, self.angle)

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
mobs = pygame.sprite.Group()
hero = Hero()
for i in range(10):
    Mob()

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