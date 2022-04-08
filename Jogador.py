from Baralho import Baralho
from PilhaEncadeada import Pilha

class JogadorException(Exception):
    def __init__(self, mensagem, metodo=''):
        super().__init__(mensagem)
        self.metodo = metodo

class Jogador:
    def __init__(self, nome):
        self.__cartasRecebidas = None
        self.__nome = nome
        self.__cartasJogadas = None
    
    def receberBaralho(self, cartas):
        self.__cartasRecebidas = Pilha()
        
        for i in range(26): #Jogador recebendo sua pilha de cartas
            self.__cartasRecebidas.empilha(cartas.retirarCarta())
            self.__quantidade += 1
        
