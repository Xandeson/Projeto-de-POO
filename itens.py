import pygame
from pygame.locals import *

tela_altura = 800
tela_largura = 800

linhas = 16
colunas = 21

TILE_SIZE = tela_altura // linhas
TILE_TYPES = 4

class Itens:
    """
    Classe que representa os itens no jogo
    """
    def __init__(self):
        """
        Inicializa a instância da classe Itens
        """
        self.tipo = []
        self.efeito = []
        self.duracao = int
        
    def aplicar_efeito(self):
        """
        Aplica o efeito do item com base no seu tipo
        """
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
        """
        Gera um novo item
        """
        self.tipo = []
        for x in range(TILE_TYPES):
            img = pygame.image.load(f'img/{x}-bloco.png')
            img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
            self.tipo.append(img)
            
    def get_tipo(self):
        return self._tipo

    def get_efeito(self):
        return self._efeito

    def get_duracao(self):
        return self._duracao

    def set_duracao(self, nova_duracao):
        self._duracao = nova_duracao