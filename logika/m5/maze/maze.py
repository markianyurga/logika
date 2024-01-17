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

player = GameSprite('hero.png', 450, 55, 6)
player2 = GameSprite('treasure.png', 450, 40, 6)
player3 = GameSprite('cyborg.png', 400, 55, 6)

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
    display.update()
    clock.tick(fps)  
    