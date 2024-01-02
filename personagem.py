from typing import Any
import pygame
from pygame.locals import *
from mixins import Sprite_player

class Player(pygame.sprite.Sprite, Sprite_player):
    def __init__(self, lista, porta):
        """
        classe que representa o personagem do boberman
        
        parametros:
            lista(world.obstacle_list): a lista de obstaculos do jogo
            porta(Porta): objeto que representa a porta do jogo
        """
        pygame.sprite.Sprite.__init__(self)
        self._vida = 3
        self._quantidade_Bomba = 3
        self._velocidade = 3
        self._list = lista
        self._x = 50
        self._y = 200
        self._sprite = self.sprites_K_dow
        self._sprit_atual = 0
        self._image = self._sprite[self._sprit_atual]
        self._rect = self._image.get_rect()
        self._rect.topleft = self._x, self._y
        self._image = pygame.transform.scale(self._image,(27*2,26*2))
        self._width = self._rect.width
        self._height = self._rect.height
        self._porta = porta
    
    def update(self, id):
        """
        atualiza a sprite do bomberman para prover a animação

        parametro:
            id(int): identificador para armazenar a sprite atual e atualiza-la
        """
        self._sprit_atual += 0.25
        if self._sprit_atual >= 7:
            self._sprit_atual = id
        self._image = self._sprite[int(self._sprit_atual)]
        self._image = pygame.transform.scale(self._image,(27*2, 26*2)) 
        
        
    def movimento(self):
        """
        movimento do jogador, utilizando decteção das teclas pressionadas e confere a colisão com os blocos
        """
        key = pygame.key.get_pressed()
        dx = 0
        dy = 0
        # movimentação pressionando as teclas
        if  key[pygame.K_DOWN]:
            dy += self._velocidade
            self.update(0)
        elif key[pygame.K_UP]:
            dy -= self._velocidade
        if key[pygame.K_RIGHT]:
            dx += self._velocidade
        elif key[pygame.K_LEFT]:
            dx -= self._velocidade
            
        old_x, old_y = self._rect.x, self._rect.y

        # Atualiza a posição do retângulo do jogador
        self._rect.x += dx
        self._rect.y += dy
        
        
        # verifica a colisão com os blocos
        for tile in self._list:
            if tile[1].colliderect(self._rect.x + dx, self._y, self._width, self._height):
                dx = 0
            if tile[1].colliderect(self._rect.x, self._y + dy, self._width, self._height):
                dy = 0
            
        self._x += dx
        self._y += dy
    
    # métodos getter e setter
    def get_vida(self):
        return self._vida

    def set_vida(self, valor):
        self._vida = valor

    def get_quantidade_bomba(self):
        return self._quantidade_bomba

    def set_quantidade_bomba(self, valor):
        self._quantidade_bomba = valor

    def get_velocidade(self):
        return self._velocidade

    def set_velocidade(self, valor):
        self._velocidade = valor

    def get_lista(self):
        return self._lista

    def set_lista(self, valor):
        self._lista = valor

    def get_x(self):
        return self._x

    def set_x(self, valor):
        self._x = valor

    def get_y(self):
        return self._y

    def set_y(self, valor):
        self._y = valor

    def get_sprite_atual(self):
        return self._sprit_atual

    def set_sprite_atual(self, valor):
        self._sprit_atual = valor

    def get_image(self):
        return self._image

    def set_image(self, valor):
        self._image = valor

    def get_rect(self):
        return self._rect

    def set_rect(self, valor):
        self._rect = valor