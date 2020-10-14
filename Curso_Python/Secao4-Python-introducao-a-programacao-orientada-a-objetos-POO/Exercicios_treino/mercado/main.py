from estoque.estoque import Stock
from financas.financa import *

if __name__ == '__main__':
    cli = Stock('Agua', 2.5, 200)
    print(cli.preco)
    cli.produtos_vendidos(180)
    cli.reposicao(50)
    cli.em_estoque()

    # cli = Dinheiro()
    print(cli.inicial)