from Baralho import Baralho
from PilhaEncadeada import Pilha

class Jogador:
    def __init__(self, nome):
        self.__cartasRecebidas = None
        self.__nome = nome
        self.__cartasJogadas = None
    
    def receberBaralho(self, cartas):
        self.__cartasRecebidas = Pilha()
        
        for i in range(26): #Jogador recebendo sua pilha de cartas
            self.__cartasRecebidas.empilha(cartas.desempilha())
            self.__quantidade += 1
        
