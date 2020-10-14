class Stock:
    def __init__(self, mercadoria, preco, quantidade):
        self.mercadoria = mercadoria
        self.preco = preco
        self.quantidade = quantidade
        self.inicial = self.quantidade

    def produtos_vendidos(self, vendas):
        self.quantidade -= vendas
        print(f'Produto vendido {self.mercadoria}: {vendas} unidades.')

    def em_estoque(self):
        print(f'Estoque Atualizado\n{self.mercadoria}: {self.quantidade} Produtos em estoque.')
        if self.quantidade <= 100:
            print(f'Repor {self.mercadoria} Abaixo do ideal.')
        else:
            print('Quantidade ideal.')

    def reposicao(self, valor):
        self.quantidade += valor
