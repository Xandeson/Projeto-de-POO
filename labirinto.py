import pygame
import os
import time
import csv
from personagem import Player
from porta import Porta

from pygame.locals import *
from sys import exit

tela_altura = 800
tela_largura = 800

tempo_inicial = 180
tempo_atual = tempo_inicial

linhas = 16
colunas = 21
TILE_SIZE = tela_altura // linhas
TILE_TYPES = 6
lvl = 1

tela = pygame.display.set_mode((tela_altura, tela_largura))

pygame.init()

fonte = pygame.font.Font(None, 30)

img_list = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'img/{x}-bloco.png')
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	img_list.append(img)


icon_bomberman = pygame.transform.scale(pygame.image.load('img/avatar_icon.png'), (25, 45))
icon_inimigo = pygame.transform.scale(pygame.image.load('img/enemy_icon.png'), (25, 60))

pygame.display.set_caption('Super Bomberman')

class World():
    """
    Classe que cria o labirinto
    """
    def __init__(self):
        """
        inicializa a intância da classe Wolrd
        """
        self._obstacle_list = []
        self._porta = 0

    def process_data(self, data):
        """
        Processa os dados do mundo

        Argumento:
            data (list): Lista contendo os dados do mundo
        """
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 4:
                        self._obstacle_list.append(tile_data)
                    if tile == 5:
                        self._porta = Porta(img, x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE)
    
    def draw(self):
        """
        Desenha o backgorund, o placar e o labirinto na tela
        """
        tela.fill((17, 123, 48))
        self._desenhar_placar()
        for tile in self._obstacle_list:
            tela.blit(tile[0], tile[1])
    
    def _desenhar_placar(self):
        """
        Desenha o placar na tela, este tem o placar, os icones do player e inimigo, e um relogio conômetro
        """
        pygame.draw.rect(tela, (255, 69, 0), (0, 0, 800, 150))
        pygame.draw.rect(tela, (255, 0, 0), (0, 0, 800, 150), 4)
        pygame.draw.rect(tela, (0, 0, 0), (170, 75, 60, 40))
        pygame.draw.rect(tela, (255, 255, 255), (170, 75, 60, 40), 2)
        pygame.draw.rect(tela, (0, 0, 0), (548, 75, 60, 40))
        pygame.draw.rect(tela, (255, 255, 255), (548, 75, 60, 40), 2)
        tela.blit(icon_bomberman, (140, 68))
        tela.blit(icon_inimigo, (515, 65))
        
        
    def get_obstacle_list(self):
        return self._obstacle_list

    def get_porta(self):
        return self._porta
    
world_data = []
for row in range(linhas):
    r = [-1] * colunas
    world_data.append(r)

with open(f'level{lvl}_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)
            
world = World() 
world.process_data(world_data)
personagem = Player(world.get_obstacle_list(), world.get_porta())      

relogio = pygame.time.Clock()


while True:
    relogio.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    world.draw()
    
    personagem.movimento()
    tela.blit(personagem.get_image(), (personagem.get_x(), personagem.get_y()))
    
    
    pygame.display.flip()