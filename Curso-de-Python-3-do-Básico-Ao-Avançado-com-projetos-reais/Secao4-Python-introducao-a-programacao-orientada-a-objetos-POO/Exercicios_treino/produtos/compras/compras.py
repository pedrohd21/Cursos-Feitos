class Produtos:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor


class Carrinho:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produtos):
        self.produtos.append(produtos)

    def lista(self):
        for prod in self.produtos:
            print(f'Produto: {prod.nome} R$:{prod.valor}')

    def soma(self):
        total = 0
        for prod in self.produtos:
            total += prod.valor
        print(f'Valor total da compra: R$ {total:.2f}')
