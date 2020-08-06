# Criar um historico de saque, transferir dinheiro


class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def saca(self, valor):
        if self.saldo < valor:
            print('Error')
        else:
            self.saldo -= valor
            print(f'Aprovado\nSaldo atual {self.saldo}')

    def deposita(self, valor):
        if self.saldo < self.limite:
            self.saldo += valor
        else:
            print('Ultrapassou o limite da conta')

    def extrato(self):
        return f'Saldo {self.saldo}'

    def transfere(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Transferencia para {destino} no valor de {valor}')
        else:
            print('Tranferencia acima do valor em conta\nTente outro valor.')



# Pagina 123