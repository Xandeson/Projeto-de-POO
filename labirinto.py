import pygame
import os

from pygame.locals import *
from sys import exit

tela_altura = 700
tela_largura = 580

tela = pygame.display.set_mode((tela_altura, tela_largura))

labirinto_img = pygame.transform.scale(pygame.image.load('img/labirinto.png'), (tela_altura, tela_largura-100))


pygame.init()
pygame.display.set_caption('Super Bomberman')

class Labirinto:
    distancia_largu = 26
    distancia_altura = 25
    
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 100
        
    def desenhar_labirinto(self):
        tela.blit(labirinto_img, (self.pos_x, self.pos_y))
        self.desenhar_placar()
        
    def desenhar_placar(self):
        pygame.draw.rect(tela, (255, 102, 0), (0, 0, 700, 100))
        
    def adicionar_blocos(self):
        pass
labirinto = Labirinto()
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    labirinto.desenhar_labirinto()
            
    pygame.display.update()