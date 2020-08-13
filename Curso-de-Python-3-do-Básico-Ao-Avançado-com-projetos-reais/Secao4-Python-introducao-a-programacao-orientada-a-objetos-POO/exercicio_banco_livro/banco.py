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
    
    def depositar(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
    
    def extrato(self):
        print(f' Numero: {self.numero}\n Saldo: {self.saldo}')

    # def transfere(self, destino, valor):
    #     self.valor -= valor
    #     destino.saldo += valor