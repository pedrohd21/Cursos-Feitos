from conta.conta_normal import Conta
from conta.conta_corrente import Corrente
from conta.conta_poupanca import Poupanca


# p1 = Cliente('Pedro', 'Henrique', '123456789')
# p1 = Conta('1234', p1.nome, 0)
# p1.depositar(100)
# p1.depositar(5000)
# p1.saca(200)
# p1.saca(200)
# p1.extrato()
#
# p1.historico.imprime()
# p1.extrato()

# p3 = Corrente(555, 555555, 50, 2000, 'masculino')
# p3.depositar(10)
# p3.extrato()
#
# p1 = Corrente(555, 555555, 50, 2000, 'masculino')
# p1.depositar(10)
# p1.extrato()

if __name__ == '__main__':
    c = Conta('123-4', 'Joao',	1000.0)
    cc = Corrente('123-5', 'Jose', 1000.0)
    cp = Poupanca('123-6', 'Maria', 1000.0)
    c.atualiza()
    cc.atualiza()
    cp.atualiza()
    print(c)
    print(cc)
    print(cp)
