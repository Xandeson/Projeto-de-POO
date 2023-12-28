import pygame
from pygame.locals import *

class Porta(pygame.sprite.Sprite):
    def __init__(self, img, x, y, TILE_SIZE):
        pygame.sprite.Sprite.__init__(self)
        self.imagem = img
        self.posicao_x = x
        self.posicao_y = y
        self.rect = self.imagem.get_rect()
        self.rect.midtop = (x + TILE_SIZE, y + (TILE_SIZE - self.imagem.get_height()))
        self.aberta = False
        
    def abrir_porta(self):
        if 0 == 0:
            self.aberta == True
            lvl += 1
            if lvl > 2:
                QUIT
        