class Lista:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco


class Sacola:
    def __init__(self):
        self.produto = []

    def adiciona(self, produto):
        self.produto.append(produto)

    def lista_produto(self):
        for c in self.produto:

            print(f'{c.produto:.<20} {c.preco}')


p1 = Lista('Notebook', 2700.00)
p2 = Lista('Tv', 4000.00)
p3 = Lista('Maquina de lavar', 1500.00)
p4 = Lista('Celular', 2700.00)

prod = Sacola()
prod.adiciona(p1)
prod.adiciona(p2)
prod.adiciona(p3)
prod.adiciona(p4)
prod.lista_produto()
