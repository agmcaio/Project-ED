# Baralho = Coleção de cartas (lista de cartas)
from Carta import Carta
from PilhaEncadeada import Pilha
from random import shuffle

class BaralhoException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)

class Baralho:
    def __init__(self):
        self.baralho = list()
        self.__baralhoEmpilhado = Pilha()

        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        numeracao = ["As","2","3","4","5","6","7","8","9","10","Valete","Dama","Rei"]

        for idx in range(len(naipe)):
            for id in numeracao:
                self.baralho.append(Carta(id, naipe[idx]))
            
    def __len__(self): 
        return self.__baralhoEmpilhado.tamanho()
    
    def temCarta(self):
        if not self.__baralhoEmpilhado.estaVazia():
            return True
        else:
            return False

    def retirarCarta(self):
       return self.__baralhoEmpilhado.desempilha()

    def embaralhar(self):
        shuffle(self.baralho)

        for carta in self.baralho:
            self.__baralhoEmpilhado.empilha(carta)
    
    def imprime(self):
        print(self.__str__())
        
    def __str__(self):
        return self.__baralhoEmpilhado