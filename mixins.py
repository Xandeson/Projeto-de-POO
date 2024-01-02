import pygame
from pygame.locals import *

class SpritePlayerMixin:
    def __init__(self):
        self._sprite = []
        self._sprit_atual = 0

    def load_sprites(self):
        self._sprite.append(pygame.image.load('sprite_player/front_1.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_2.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_3.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_4.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_5.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_6.png'))
        self._sprite.append(pygame.image.load('sprite_player/front_7.png'))


    def get_image(self):
        return self._image
