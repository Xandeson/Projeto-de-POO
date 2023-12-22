class Bomba:
    __alcance_explosao = 3
    __tempo_explosao = 5
    __detonar = False
        
    def set_detonar(self):
        self.__detonar = True

    def detona_bamba(self):
        self.set_detonar()


class Itens:
    def __init__(self, x, y, efeito):
        self.x = x
        self.y = y
        self.efeito = efeito

    def item_efeito(efeito, Personagem):
        if efeito ==  1:
            pass   #fazer tabela de efeito
        elif efeito == 2:
            pass
        elif efeito == 3:
            pass
        elif efeito == 4:
            pass
        elif efeito == 5:
            pass