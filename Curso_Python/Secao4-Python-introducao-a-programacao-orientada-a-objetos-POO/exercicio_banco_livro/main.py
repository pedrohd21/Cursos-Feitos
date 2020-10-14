from banco import *


# p1 = Conta('123-4', 'Pedro', 120.0, 1000.0)
# p1.saca(20)
# p1.depositar(50)
# p1.extrato()

# p2 = Cliente('João', 'Oliveira', '1111111-1')

cliente1 = Cliente('João',	'Oliveira',	'11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1, 1000.0)
conta2 = Conta('123-5', cliente2, 1000.0)
conta1.depositar(100.0)
conta1.saca(5000)
conta1.transfere(conta2, 200.0)
conta1.extrato()

conta1.historico.imprime()

conta2.historico.imprime()