from conta.conta_normal import Conta


class Poupanca(Conta):
    def __init__(self, numero, titular, saldo, limite=5000):
        Conta.__init__(self, numero, titular, saldo, limite)

    def atualiza(self, taxa=0.03):
        Conta.atualiza(self, taxa)
        # return self.saldo

    def __str__(self):
        return f'Dados da Conta: \nNumero: {self.numero} \nSaldo: {self._saldo} R$ \nLimite: {self._limite} \n{"-"*30}'

