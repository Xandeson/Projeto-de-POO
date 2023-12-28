import pygame
from pygame.locals import *

tela_altura = 800
tela_largura = 800

linhas = 16
colunas = 21

TILE_SIZE = tela_altura // linhas
TILE_TYPES = 4

class Itens:
    def __init__(self):
        self.tipo = []
        self.efeito = []
        self.duracao = int
        
    def aplicar_efeito(self):
        if self.tipo == self.tipo[0]:
            pass
            #self.efeito[0] tamanho da bomba aumenta
        elif self.tipo == self.tipo[1]:
            #quantidade de bombas
            pass
        elif self.tipo == self.tipo[2]:
            #vida
            pass
        elif self.tipo == self.tipo[3]:
            #velocidade
            pass
        
    def gerar_item(self):
        self.tipo = []
        for x in range(TILE_TYPES):
            img = pygame.image.load(f'img/{x}-bloco.png')
            img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
            self.tipo.append(img)