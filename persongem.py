#import pygame

class Personagem:
    _itens = []
    def __init__(self, nome, posicao,vida, quantidade_Bomba):
        self.nome = nome
        self.posicao = posicao
        self.vida = vida
        self.quantidade_Bomba = quantidade_Bomba
        self._velocidade = 3

    def posicionar_bomba():
        pass

    def mover():
        pass

    def adicionar_item(self,valor):
        self._itens.append(valor)

    def morte(self):
        if self.vida == 0:
            pass #game over