from datetime import datetime


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Deposito de: R$ {valor}')
        return

    def saca(self, valor):
        self.saldo -= valor
        self.historico.transacoes.append(f'Saque de: R$ {valor}')
        return

    def extrato(self):
        print(f' Saldo em conta: R$ {self.saldo}')


class Historico:
    def __init__(self):
        self.data_abertura = datetime.today().strftime('Dia %d/%m/%Y Horas %H:%M')
        self.transacoes = []

    def imprime(self):
        print(f'Historico de transações')
        print(f'Data de abertura: {self.data_abertura} ')

        for c in self.transacoes:
            print('-', c)
