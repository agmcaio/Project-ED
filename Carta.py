class Carta:
    def __init__(self, numero, naipe):
        self.__numero = numero
        self.__naipe = naipe
    
    @property
    def naipe(self):
        return self.__naipe
    
    @property
    def numero(self):
        return self.__numero
    
    def __str__(self):
        return str(self.__numero) + " de " + self.__naipe