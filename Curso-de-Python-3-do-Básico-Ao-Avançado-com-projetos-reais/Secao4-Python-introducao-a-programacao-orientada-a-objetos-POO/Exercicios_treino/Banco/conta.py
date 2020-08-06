class Conta:
    def __init__(self, numero, titulo, saldo, limite=1000.0):
        self._numero = numero
        self._titulo = titulo
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
        if valor < 0:
            print('Nn pode ter saldo negativo')


p1 = Conta('158-7', '9999', -5, 800)
print(p1.saldo)

