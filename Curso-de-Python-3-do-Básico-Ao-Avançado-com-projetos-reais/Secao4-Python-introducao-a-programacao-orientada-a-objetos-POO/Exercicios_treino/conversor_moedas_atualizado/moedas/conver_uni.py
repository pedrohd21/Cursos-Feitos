class Moedas:
    def __init__(self, dinheiro):
        self._dinheiro = dinheiro

    @property
    def dinheiro(self):
        return self._dinheiro

    def realXeua(self):
        resultado = self.dinheiro / 5.34
        return f'R$ {resultado:.2f}'

    def euaXreal(self):
        resultado = self.dinheiro * 5.34
        return f'U$ {resultado:.2f}'

    def euaXreal(self):
        resultado = self.dinheiro * 5.34
        return f'U$ {resultado:.2f}'
