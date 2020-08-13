from banco import *

p1 = Conta('123-4', 'Pedro', 120.0, 1000.0)
p1.saca(20)
p1.depositar(50)
p1.extrato()

p2 = Cliente('João', 'Oliveira', '1111111-1')

print(type(p1.numero))