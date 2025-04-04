import pygame, random, os

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'hero.png'))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.45)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = SCENE_HEIGHT - 20
        all_sprites.add(self)
        now = pygame.time.get_ticks()
        self.last_shoot = now
        self.shoot_delay = 1000

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
        if pressed[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.last_shoot = now

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = random.choice(['small', 'middle', 'big'])
        path = os.path.join(IMG_DIR, 'mobs', self.size)
        filenames = os.listdir(path)
        self.img = pygame.image.load(
            os.path.join(path, random.choice(filenames))
        ).convert_alpha()
        self.image = self.img
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.36)
        self.rect.center = (
            random.randint(-100, WIDTH + 100),
            random.randint(-100, 0)
        )
        self.vx = random.randint(-1, 1)
        self.vy = random.randint(1, 5)
        self.vr = random.randint(-3, 3)
        self.angle = 0
        self.animation_rate = 100
        self.last_update = pygame.time.get_ticks()
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
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_rate:
            self.angle = (self.angle + self.vr) % 360
            old_center = self.rect.center
            self.image = pygame.transform.rotate(self.img, self.angle)
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.last_update = now

class Explosion(pygame.sprite.Sprite):
    def __init__(self, coords, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[size][0]
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        all_sprites.add(self)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                self.image = explosion_anim[self.size][self.frame]

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10
        all_sprites.add(self)
        bullets.add(self)

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

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
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()
hero = Hero()
for i in range(5):
    Mob()

explosion_anim = {'sm': [], 'lg': [], 'player': []}
for i in range(9):
    filename = f'regularExplosion0{i}.png'
    img = pygame.image.load(os.path.join(IMG_DIR, 'explosions', filename)).convert_alpha()
    img_lg = pygame.transform.scale(img, (75, 75))
    img_sm = pygame.transform.scale(img, (30, 30))
    explosion_anim['lg'].append(img_lg)
    explosion_anim['sm'].append(img_sm)

bullet_img = pygame.image.load(os.path.join(IMG_DIR, 'bullet.png')).convert_alpha()

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

    # столкновение игрока с мобами
    for mob in pygame.sprite.spritecollide(hero, mobs, True, pygame.sprite.collide_circle):
        expl = Explosion(mob.rect.center, 'sm')
        Mob()
    
    # столкновение пули с мобами
    for hit in pygame.sprite.groupcollide(mobs, bullets, True, True):
        Explosion(hit.rect.center, 'lg')
        Mob()
    
    # render
    info.fill((0, 0, 100))
    scene.fill((0, 0, 0))
    all_sprites.draw(scene)
    screen.blit(info, (0, 0, WIDTH, INFO_HEIGHT))
    screen.blit(scene, (0, INFO_HEIGHT, WIDTH, HEIGHT))
    pygame.display.flip()

pygame.quit()