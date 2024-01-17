#створи гру "Лабіринт"!
from pygame import *
from pygame.sprite import collide_rect, Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

class GameSprite(Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = scale(load(image), [82, 80])
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        WINDOW.blit(self.image,[self.rect.x, self.rect.y])

class Player(GameSprite):
    def update(self):
        pressed = key.get_pressed()
        if pressed[K_UP]:
            self.rect.y -= self.speed
            
        if pressed[K_DOWN]:
            self.rect.y += self.speed
            
        if pressed[K_LEFT]:
            self.rect.x -= self.speed
            
        if pressed[K_RIGHT]:
            self.rect.x += self.speed
        
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        
        if self.direction == 'right':
            self.rect.x += self.speed
         

player = Player('hero.png', 10, 10, 6)
player2 = GameSprite('treasure.png', 660, 400, 6)
player3 = Enemy('cyborg.png', 660, 311, 6)

WINDOW = display.set_mode([750, 500])

background = scale(load('background.jpg'), [750, 500])

game = True

clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    WINDOW.blit(background, [0, 0])
    player.reset()
    player2.reset()
    player3.reset()
    
    player.update()
    player3.update()
    
    display.update()
    clock.tick(fps)  
    