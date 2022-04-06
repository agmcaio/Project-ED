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

        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        numeracao = ["As","2","3","4","5","6","7","8","9","10","Valete","Dama","Rei"]

        for idx in range(len(naipe)):
            for id in numeracao:
                self.baralho.append(Carta(id, naipe[idx]))
            
    def __len__(self): 
        return self.baralho.tamanho()
    
    def temCarta(self):
        if len(self.baralho) > 0:
            return True

        return False
    
    def retirarCarta(self):
        if self.temCarta():
            return self.baralho.pop()
        else:
            raise BaralhoException("Não há cartas no baralho")

    def embaralhar(self):
        import random
        random.shuffle(self.baralho)
    
    def imprime(self):
        print(self.baralho)
        
        
if __name__ == "__main__":
    test = Baralho()
    test.embaralhar()
    test.imprime()
    print(f'Há cartas? {test.temCarta()}')
    for i in range(52):
        print(test.retirarCarta())  # retira carta do baralho
    print(f'Há cartas? {test.temCarta()}')
    test.imprime()