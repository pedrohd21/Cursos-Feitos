from random import randint


class MaiorMenor:
    def __init__(self):
        self.numeros = []

    def sorteia(self):
        for c in range(10):
            rand = randint(1, 100)
            self.numeros.append(rand)
        print(f'Numeros Sorteados: {self.numeros}')

    def maior(self):
        maior = max(self.numeros)
        print('Maior numero sorteado: ', maior)

    def menor(self):
        menor = min(self.numeros)
        print('Menor numero sorteado: ', menor)


a = MaiorMenor()
a.sorteia()
a.maior()
a.menor()