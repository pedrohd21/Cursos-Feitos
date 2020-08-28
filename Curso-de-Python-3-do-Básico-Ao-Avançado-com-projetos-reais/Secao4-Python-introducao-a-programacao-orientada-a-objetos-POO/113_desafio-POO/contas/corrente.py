from contas.conta import Bank


class Banco(Bank):
    def __init__(self, saldo, limite=200):
        super().__init__(saldo, limite)

    def depositar(self, valor):
        if valor < self.limite:
            self.saldo += valor

    def sacar(self, valor):
        if valor < self.limite:
            self.saldo -= valor


