from compras.compras import *

p1 = Produtos('Apple', 25)
p2 = Produtos('Laranja', 90)
p4 = Produtos('Smartphone',  700)
p5 = Produtos('Pc', 5000)
p6 = Produtos('Espanador', 10)
p7 = Produtos('Refrigerante', 10)
p8 = Produtos('Minha vida', 0)

carrinho = Carrinho()
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p4)
carrinho.inserir_produtos(p5)
carrinho.inserir_produtos(p6)
carrinho.inserir_produtos(p7)
carrinho.inserir_produtos(p8)
carrinho.lista()
carrinho.soma()