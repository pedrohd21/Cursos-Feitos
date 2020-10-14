from datetime import datetime


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, titular, saldo=0, limite=3000):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @ saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            print('Saldo nn pode ser negativo.')
        else:
            self._saldo = float(valor)

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, valor):
        self._historico = valor

    def depositar(self, valor):
        self._saldo += valor
        if self._saldo > self._limite:
            print(f'Acima do Limite permitido de R$ {self._limite}')
            self._saldo -= valor
        else:
            self._historico.transacoes.append(f'Deposito de: R$ {valor}')
            return

    def saca(self, valor):
        self._saldo -= valor
        self._historico.transacoes.append(f'Saque de: R$ {valor}')
        return

    def extrato(self):
        print(f' Saldo em conta: R$ {self._saldo}')

    def atualiza(self, taxa=0):
        self._saldo += (self._saldo * taxa)
        # return self.saldo

    def __str__(self):
        return f'{"-"*30} \nDados da Conta: \nNumero: {self.numero} \nSaldo: {self._saldo} R$ \nLimite: {self._limite} \n{"-"*30}'


class Historico:
    def __init__(self):
        self.data_abertura = datetime.today().strftime('Dia %d/%m/%Y Horas %H:%M')
        self.transacoes = []

    def imprime(self):
        print(f'Historico de transações')
        print(f'Data de abertura: {self.data_abertura} ')

        for c in self.transacoes:
            print('-', c)
