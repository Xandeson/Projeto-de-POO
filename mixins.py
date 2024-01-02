import pygame
from pygame.locals import *

class Sprite_player:
    def sprites_K_dow(self):
        self._sprite = []
        self._sprite.append(pygame.image.load('sprite_player/front_1.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_2.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_3.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_4.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_5.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_6.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_7.png'))