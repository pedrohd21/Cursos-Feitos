class Conta:
    def __init__(self, numero, titulo, saldo, limite=1000.0):
        self.numero = numero
        self.titulo = titulo
        self.saldo = saldo
        self.limite = limite

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
        pass

    def deposita(self, valor):
        self.saldo += valor

    def saca(self):
        pass

    def extrato(self):
        pass

    def transfere_para(self):
        pass


p1 = Conta


print('OI beleza mundo agua pessoas abobora futebol ')



