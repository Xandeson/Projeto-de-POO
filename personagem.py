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
        self.x = 80
        self.y = 120
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
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale2x(self.image)
    
    def update(self):
        self.sprit_atual += 1
        if self.sprit_atual >= len(self.sprite):
            self.sprit_atual = 0
        self.image = self.sprite[int(self.sprit_atual)]
        self.image = pygame.transform.scale2x(self.image) 
        
    def movimento(self):
        self.image = pygame.transform.scale2x(self.image)
        key = pygame.key.get_pressed()
        dist = 5 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
        

 
    #def movimento(self):
