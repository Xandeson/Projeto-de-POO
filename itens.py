from personagem import Player
class Itens:
    def __init__(self):
        self.tipo = []
        self.efeito = ""
        self.duracao = int
        
    def aplicar_efeito(self):
        if self.efeito == self.tipo[0]:
            pass
        elif self.efeito == self.tipo[1]:
            pass
        elif self.efeito == self.tipo[2]:
            pass
        elif self.efeito == self.tipo[3]:
            pass
        else:
            pass
        
    def gerar_item(self):
        self.tipo