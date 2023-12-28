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
    def __init__(self, list, porta):
        pygame.sprite.Sprite.__init__(self)
        self.list = list
        self.x = 50
        self.y = 200
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
        self.update(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image,(27*2,26*2))
        self.width = self.rect.width
        self.height = self.rect.height
        self.porta = porta
    
    def update(self,id):
        self.sprit_atual += 0.25
        if self.sprit_atual >= 7:
            self.sprit_atual = id
        self.image = self.sprite[int(self.sprit_atual)]
        self.image = pygame.transform.scale2x(self.image) 
        
        
    def movimento(self):
        key = pygame.key.get_pressed()
        dist = 10
        dx = 0
        dy = 0# distance moved in 1 frame, try changing it to 5
        if  key[pygame.K_DOWN]: # down key
            dy += dist # move down
            self.update(0)
        elif key[pygame.K_UP]: # up key
            dy -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            dx += dist # move right
        elif key[pygame.K_LEFT]: # left key
            dx -= dist # move left
            
        for tile in self.list:
            if tile[1].colliderect(self.rect.x + dx, self.y, 0, 0):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.y + dy, 0, 0):
                dy = 0
            
        self.rect.x += dx
        self.rect.y += dy
        
        
        #if pygame.sprite.spritecollide(self, porta, False):
         #   self.porta.aberta = True