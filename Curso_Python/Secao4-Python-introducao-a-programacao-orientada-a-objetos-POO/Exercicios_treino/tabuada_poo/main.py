class Tabuada:
    def __init__(self, n1):
        self._n1 = n1

    @property
    def n1(self):
        return self._n1

    def gerando(self):
        for c in range(0, 10):
            print(f'{self.n1} x {c} = {int(self.n1) * c}')


numeros = Tabuada(5)
numeros.gerando()