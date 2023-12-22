import pygame
import os

from pygame.locals import *
from sys import exit

tela_altura = 700
tela_largura = 490

tela = pygame.display.set_mode((tela_altura, tela_largura))
bg_verde = (16, 121, 49)

pygame.init()
pygame.display.set_caption('Super Bomberman')

class Labirinto:
    distancia_largu = 26
    distancia_altura = 25
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.parede
        
    def desenhar_labirinto(self):
       pass
        
    def desenhar_placar(self):
        pygame.draw.rect(tela, (255, 102, 0), (0, 0, 700, 100))
        
    def adicionar_blocos(self):
        pass
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.display.update()