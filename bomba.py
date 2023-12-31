from typing import Any
import pygame
from pygame.locals import *
from sys import exit

class Bomba(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    
        self.posicao_x = 80
        self.posicao_y = 120
        #self.explodir = False
        self.sprite = []
        self.sprite.append(pygame.image.load('sprite_bomba/bomba_0.png'))
        self.sprite.append(pygame.image.load('sprite_bomba/bomba_1.png'))
        self.sprite.append(pygame.image.load('sprite_bomba/bomba_2.png'))
        self.sprit_atual = 0
        self.update()
        self.image = self.sprite[int(self.sprit_atual)]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.posicao_x, self.posicao_y
        self.image = pygame.transform.scale(self.image,(27*2,26*2))
    
    def update(self):
        self.sprit_atual += 0.1
        if self.sprit_atual >= len(self.sprite):
            self.sprit_atual = 0
        self.image = self.sprite[int(self.sprit_atual)]
        self.image = pygame.transform.scale2x(self.image)
        print("ok")

    #def explosao(self):
    #     self.explodir == True

    