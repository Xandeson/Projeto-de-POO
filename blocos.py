import pygame
import os

from pygame.locals import *
from sys import exit

tela_altura = 700
tela_largura = 490

class Bloco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprites.Sprite.__init__(self)
        self.tipo_bloco = []
        self.tipo_bloco.append(pygame.image.load('img/bloco_borda.png'))
        self.destrutivel = bool
        self.atual = 0
        self.image = self.tipo_bloco[self.atual]
    
    def pegar_bloco(self):
        if self.bool == False:
            self.atual = 0
            self.image = self.tipo_bloco[self.atual]
        else:
            self.atual = 1
            self.image = self.tipo_bloco[self.atual]

    def construtor(self):
        tamanho_bloco = 25
        for x in range(tela_largura), 25:
            for y in range(tela_altura), 25:
                pass
        
    def destruidor(self):
        if self.bool == True:
            pass