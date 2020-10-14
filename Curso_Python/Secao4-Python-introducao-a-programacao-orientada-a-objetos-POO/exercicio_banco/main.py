from conta.conta import Conta
from conta.cliente import *

if __name__ == '__main__':
    p1 = Conta('123-4', 'Pedro', 1200, 1000)
    print(p1.numero)
    print(p1.titulo)
    print(p1.saldo)
    print(p1.limite)

