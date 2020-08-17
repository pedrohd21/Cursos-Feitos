import datetime


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    total_contas = 1

    def __init__(self, numero, titular, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de {valor}')
    
    def saca(self, valor):
        if (self.saldo < valor):
            print('Operão falhou')
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'Depósito de {valor}')
    
    def extrato(self):
        print(f' Numero: {self.numero}\n Saldo: {self.saldo}')
        self.historico.transacoes.append(f'Tirou extrato - saldo de {self.saldo} ')

    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append(f'Transferencia de {valor} para conta {destino.numero}')
            return True


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'Data abertura: {self.data_abertura}')
        print('Transações: ')
        for t in self.transacoes:
            print('-', t)