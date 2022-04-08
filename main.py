from Baralho import Baralho
from Jogador import Jogador

baralho = Baralho()
baralho.embaralhar()
baralho.imprime()
print(f'Tem cartas? {baralho.temCarta()}')
print(f'Quantidade: {len(baralho)}')
for i in range(50):
    print(f'{baralho.retirarCarta()}')
    baralho.imprime()
print(f'Quantidade: {len(baralho)}')
baralho.imprime()
