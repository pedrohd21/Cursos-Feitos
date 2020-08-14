from dados.dados import *


p1 = Cliente('Pedro', 'Henrique', '123456789')
p1 = Conta('1234', p1.nome, 500)
p1.depositar(100)
p1.depositar(100)
p1.saca(200)
p1.saca(200)
p1.extrato()

p1.historico.imprime()
p1.extrato()
