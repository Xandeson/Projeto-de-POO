from typing import Any
import pygame
from pygame.locals import *
from sys import exit

class Personagem:
    _itens = []
    def __init__(self, nome, posicao,vida, quantidade_Bomba):
        self.nome = nome
        self.posicao = posicao
        self.vida = vida
        self.quantidade_Bomba = quantidade_Bomba
        self._velocidade = 3

    def posicionar_bomba():
        pass

    def mover():
        pass

    def adicionar_item(self,valor):
        self._itens.append(valor)

    def morte(self):
        if self.vida == 0:
            pass #game over
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = []
        self.sprite.append(pygame.image.load('sprite_player/front_1.png'))
        self.sprite.append(pygame.image.load('sprite_player/front_2.png'))
        self.sprite.append(pygame.image.load('sprite_player/front_3.png'))
        self.sprite.append(pygame.image.load('sprite_player/front_4.png'))
        self.sprite.append(pygame.image.load('sprite_player/front_5.png'))
        self.sprite.append(pygame.image.load('sprite_player/front_6.png'))
        self.sprite.append(pygame.image.load('sprite_player/front_7.png'))
        self.sprit_atual = 0
        self.image = self.sprite[self.sprit_atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 80, 120
        self.image = pygame.transform.scale2x(self.image)
    
    def update(self):
        self.sprit_atual += 0.1
        if self.sprit_atual >= len(self.sprite):
            self.sprit_atual = 0
        self.image = self.sprite[int(self.sprit_atual)]
        self.image = pygame.transform.scale(self.image, (27*2,26*2)) 

 
    #def movimento(self):
