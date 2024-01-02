import pygame
from pygame.locals import *

class Porta(pygame.sprite.Sprite):
    def __init__(self, img, x, y, TILE_SIZE):
        """
        inicia a classe Porta.

        Parameters:
            img(pygame.Surface): imagem da porta
            x(int): coordenada x da posição da porta
            y(int): coordenada y da posição da porta
            TILE_SIZE(int): O tamanho do bloco
        """
        pygame.sprite.Sprite.__init__(self)
        self.imagem = img
        self._posicao_x = x
        self._posicao_y = y
        self.rect = self.imagem.get_rect()
        self.rect.midtop = (x + TILE_SIZE, y + (TILE_SIZE - self.imagem.get_height()))
        self._aberta = False

    # métodos getter e setter
    def get_posicao_x(self):
        return self._posicao_x

    def get_posicao_y(self):
        return self._posicao_y

    def get_rect(self):
        return self.rect

    def esta_aberta(self):
        return self._aberta

    def abrir_porta(self):
        """
        Abre a porta.

        Se a porta for aberta, aumenta o nível (lvl) global.
        Se o nível for maior que 2, encerra o jogo.
        """
        if not self._aberta:
            self._aberta = True
            global lvl
            lvl += 1
            if lvl > 2:
                pygame.quit()
                exit()

    def fechar_porta(self):
        """
        Fecha a porta.

        Se a porta estiver aberta, fecha a porta, assim ao começar uma nova fase a porta não irá começar aberta
        """
        if self._aberta:
            self._aberta = False
