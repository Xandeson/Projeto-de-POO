import pygame
import os
import time
import csv
from personagem import Player

from pygame.locals import *
from sys import exit

tela_altura = 800
tela_largura = 800

tempo_inicial = 180
tempo_atual = tempo_inicial

linhas = 16
colunas = 21
TILE_SIZE = tela_altura // linhas
TILE_TYPES = 13
lvl = 1

tela = pygame.display.set_mode((tela_altura, tela_largura))

pygame.init()

fonte = pygame.font.Font(None, 30)

img_list = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'img/{x}-bloco.png')
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	img_list.append(img)

save_img = pygame.image.load('img/save_btn.png').convert_alpha()
load_img = pygame.image.load('img/load_btn.png').convert_alpha()

labirinto_img = pygame.transform.scale(pygame.image.load('img/labirinto.png'), (tela_altura, tela_largura-100))
icon_bomberman = pygame.transform.scale(pygame.image.load('img/avatar_icon.png'), (25, 45))
icon_inimigo = pygame.transform.scale(pygame.image.load('img/enemy_icon.png'), (25, 60))


pygame.display.set_caption('Super Bomberman')

class World():
    def __init__(self):
        self.obstacle_list = []
        
    def process_data(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 5:
                        self.obstacle_list.append(tile_data)
    
    def draw(self):
        tela.fill((17, 123, 48))
        self.desenhar_placar()
        for tile in self.obstacle_list:
            tela.blit(tile[0], tile[1])
    
    def desenhar_placar(self):
        pygame.draw.rect(tela, (255, 69, 0), (0, 0, 800, 150))
        pygame.draw.rect(tela, (255, 0, 0), (0, 0, 800, 150), 4)
        pygame.draw.rect(tela, (0, 0, 0), (170, 75, 60, 40))
        pygame.draw.rect(tela, (255, 255, 255), (170, 75, 60, 40), 2)
        pygame.draw.rect(tela, (0, 0, 0), (355, 75, 60, 40))
        pygame.draw.rect(tela, (255, 255, 255), (355, 75, 60, 40), 2)
        pygame.draw.rect(tela, (0, 0, 0), (548, 75, 60, 40))
        pygame.draw.rect(tela, (255, 255, 255), (548, 75, 60, 40), 2)
        tela.blit(icon_bomberman, (140, 68))
        tela.blit(icon_inimigo, (515, 65))


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
personagem = Player()      

relogio = pygame.time.Clock()
while True:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #labirinto.desenhar_labirinto()
    world.draw()
    
    personagem.movimento()
    tela.blit(personagem.image, (personagem.x, personagem.y))
    
    clock = pygame.time.Clock()
            
    tempo_atual = max(0, tempo_atual - 1)

    minutos = tempo_atual // 60
    segundos = tempo_atual % 60

    texto = fonte.render(f"{minutos:02}:{segundos:02}", True, (255, 255, 255))
    texto_retangulo = texto.get_rect(center=(385, 95))
    tela.blit(texto, texto_retangulo)

    pygame.display.flip()

    clock.tick(1)
    
    
