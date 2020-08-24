from conta.conta_normal import Conta


class Corrente(Conta):
    def __init__(self, numero, titular, saldo, limite=5000):
        Conta.__init__(self, numero, titular, saldo, limite)

    def atualiza(self, taxa=0.02):
        Conta.atualiza(self, taxa)
        # return self.saldo

    def depositar(self, valor):
        Conta.depositar(self, valor)
        self._saldo -= 0.10

    def __str__(self):
        return f'Dados da Conta: \nNumero: {self.numero} \nSaldo: {self._saldo} R$ \nLimite: {self._limite} \n{"-"*30}'
