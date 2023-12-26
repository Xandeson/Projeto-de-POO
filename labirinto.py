import pygame
import os
import time

from pygame.locals import *
from sys import exit

tela_altura = 700
tela_largura = 580

tempo_inicial = 180
tempo_atual = tempo_inicial

tela = pygame.display.set_mode((tela_altura, tela_largura))

pygame.init()

fonte = pygame.font.Font(None, 30)

labirinto_img = pygame.transform.scale(pygame.image.load('img/labirinto.png'), (tela_altura, tela_largura-100))
icon_bomberman = pygame.transform.scale(pygame.image.load('img/avatar_icon.png'), (25, 45))
icon_inimigo = pygame.transform.scale(pygame.image.load('img/enemy_icon.png'), (25, 60))


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
        pygame.draw.rect(tela, (255, 69, 0), (0, 0, 700, 100))
        pygame.draw.rect(tela, (255, 0, 0), (0, 0, 700, 100), 4)
        pygame.draw.rect(tela, (0, 0, 0), (134, 25, 60, 40))
        pygame.draw.rect(tela, (255, 255, 255), (134, 25, 60, 40), 2)
        pygame.draw.rect(tela, (0, 0, 0), (325, 25, 60, 40))
        pygame.draw.rect(tela, (255, 255, 255), (325, 25, 60, 40), 2)
        pygame.draw.rect(tela, (0, 0, 0), (518, 25, 60, 40))
        pygame.draw.rect(tela, (255, 255, 255), (518, 25, 60, 40), 2)
        tela.blit(icon_bomberman, (96, 18))
        tela.blit(icon_inimigo, (480, 15))
        
    def adicionar_blocos(self):
        pass
labirinto = Labirinto()
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    labirinto.desenhar_labirinto()
    clock = pygame.time.Clock()
            
    tempo_atual = max(0, tempo_atual - 1)

    minutos = tempo_atual // 60
    segundos = tempo_atual % 60

    texto = fonte.render(f"{minutos:02}:{segundos:02}", True, (255, 255, 255))
    texto_retangulo = texto.get_rect(center=(355, 45))
    tela.blit(texto, texto_retangulo)

    pygame.display.flip()

    clock.tick(1)