from typing import Any
import pygame
from pygame.locals import *
from sys import exit
from bomba import Bomba

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
        self.sprite.append(pygame.image.load('sprite_player/right_1.png'))
        self.sprite.append(pygame.image.load('sprite_player/right_2.png'))
        self.sprite.append(pygame.image.load('sprite_player/right_3.png'))
        self.sprite.append(pygame.image.load('sprite_player/right_4.png'))
        self.sprite.append(pygame.image.load('sprite_player/right_5.png'))
        self.sprite.append(pygame.image.load('sprite_player/right_6.png'))
        self.sprite.append(pygame.image.load('sprite_player/right_7.png'))
        self.sprite.append(pygame.image.load('sprite_player/left_1.png'))
        self.sprite.append(pygame.image.load('sprite_player/left_2.png'))
        self.sprite.append(pygame.image.load('sprite_player/left_3.png'))
        self.sprite.append(pygame.image.load('sprite_player/left_4.png'))
        self.sprite.append(pygame.image.load('sprite_player/left_5.png'))
        self.sprite.append(pygame.image.load('sprite_player/left_6.png'))
        self.sprite.append(pygame.image.load('sprite_player/left_7.png'))
        self.sprite.append(pygame.image.load('sprite_player/back_1.png'))
        self.sprite.append(pygame.image.load('sprite_player/back_2.png'))
        self.sprite.append(pygame.image.load('sprite_player/back_3.png'))
        self.sprite.append(pygame.image.load('sprite_player/back_4.png'))
        self.sprite.append(pygame.image.load('sprite_player/back_5.png'))
        self.sprite.append(pygame.image.load('sprite_player/back_6.png'))
        self.sprite.append(pygame.image.load('sprite_player/back_7.png'))
        self.sprit_atual = 0
        self.image = self.sprite[self.sprit_atual]
        self.update(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image,(27*2,26*2))
        self.bomb = Bomba

    
    def update(self,id):
        self.sprit_atual += 0.25
        if self.sprit_atual >= id + 7:
            self.sprit_atual = id
        self.image = self.sprite[int(self.sprit_atual)]
        self.image = pygame.transform.scale2x(self.image) 
        
        
    def movimento(self):
        key = pygame.key.get_pressed()
        dist = 5 # distance moved in 1 frame, try changing it to 5
        if  key[pygame.K_DOWN]: # down key
            self.y += dist # move down
            self.update(0)
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
            self.update(21)
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
            self.update(7)
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
            self.update(14)
        
            
    #def movimento(self):
